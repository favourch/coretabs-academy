from rest_framework.test import APITestCase
from django.shortcuts import reverse

from rest_framework.authtoken.models import Token

from .serializers import TokenSerializer, UserDetailsSerializer
from .tokens import confirm_email_token_generator
from django.utils.http import int_to_base36

from django.core import mail
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupTestCase(APITestCase):

    def setUp(self):
        self.payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password1': 'test1234',
            'password2': 'test1234',
            'name': 'Test User'
        }

    def test_signup_view_returns_201(self):
        response = self.client.post(reverse('registration'), self.payload)

        self.assertEqual(response.status_code, 201)

    def test_signup_creates_user(self):
        initial_users_count = User.objects.all().count()
        self.client.post(reverse('registration'), self.payload)

        self.assertEqual(User.objects.all().count(), initial_users_count + 1)

    def test_signup_creates_email_address(self):
        self.client.post(reverse('registration'), self.payload)

        user = User.objects.get(username=self.payload['username'])

        # raises error if not found
        user.email_addresses.get(primary=True)

    def test_signup_creates_account(self):
        self.client.post(reverse('registration'), self.payload)

        user = User.objects.get(username=self.payload['username'])

        # raises error if not found
        user.account

    def test_signup_creates_token(self):
        self.client.post(reverse('registration'), self.payload)

        user = User.objects.get(username=self.payload['username'])

        # raises error if not found
        user.auth_token

    def test_signup_sends_confirmation_email(self):
        initial_mails_count = len(mail.outbox)

        self.client.post(reverse('registration'), self.payload)

        self.assertEqual(len(mail.outbox), initial_mails_count + 1)
        self.assertEqual(mail.outbox[initial_mails_count].subject, 'تأكيد الحساب')

    def test_signup_name_validation(self):
        responses = []

        self.payload['name'] = 'Test'
        responses.append(self.client.post(reverse('registration'), self.payload))

        self.payload['name'] = 'Test User.'
        responses.append(self.client.post(reverse('registration'), self.payload))

        for response in responses:
            self.assertEqual(response.status_code, 400)

    def test_signup_username_validation(self):
        responses = []

        self.payload['username'] = ''
        responses.append(self.client.post(reverse('registration'), self.payload))

        self.payload['username'] = 'ts'
        responses.append(self.client.post(reverse('registration'), self.payload))

        self.payload['username'] = 'user'
        self.client.post(reverse('registration'), self.payload)
        responses.append(self.client.post(reverse('registration'), self.payload))

        for response in responses:
            self.assertEqual(response.status_code, 400)

    def test_signup_email_validation(self):
        responses = []

        self.payload['email'] = 'bad_email@user'
        responses.append(self.client.post(reverse('registration'), self.payload))

        self.payload['email'] = 'user@test.com'
        self.client.post(reverse('registration'), self.payload)
        responses.append(self.client.post(reverse('registration'), self.payload))

        for response in responses:
            self.assertEqual(response.status_code, 400)

    def test_signup_password_validation(self):
        responses = []

        self.payload['password1'] = 'test123'
        responses.append(self.client.post(reverse('registration'), self.payload))

        self.payload['password1'] = '12345678'
        responses.append(self.client.post(reverse('registration'), self.payload))

        self.payload['password1'] = 'test1234'
        self.payload['password2'] = 'test12345'
        responses.append(self.client.post(reverse('registration'), self.payload))

        for response in responses:
            self.assertEqual(response.status_code, 400)


class VerifyEmailTestCase(APITestCase):
    def setUp(self):
        self.signup_payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password': 'test1234',
            'first_name': 'Test User'
        }

        self.user = User.objects.create_user(**self.signup_payload)
        self.email = self.user.email_addresses.get(primary=True)

    def _create_uid_and_token(self, email):
        token = confirm_email_token_generator.make_token(email)
        uid = int_to_base36(email.pk)

        return token, uid

    def test_email_not_verified_after_signup(self):
        self.assertFalse(self.email.verified)

    def test_verify_email_returns_200(self):
        token, uid = self._create_uid_and_token(self.email)

        response = self.client.post(reverse('verify_email'), {
            'key': token,
            'uid': uid
        })

        self.assertEqual(response.status_code, 200)

    def test_verify_email_verifies_email(self):
        token, uid = self._create_uid_and_token(self.email)

        self.client.post(reverse('verify_email'), {
            'key': token,
            'uid': uid
        })
        email = self.user.email_addresses.get(primary=True)

        self.assertTrue(email.verified)


class ResendConfirmTestCase(APITestCase):
    def setUp(self):
        self.signup_payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password': 'test1234',
            'first_name': 'Test User'
        }

        self.user = User.objects.create_user(**self.signup_payload)

    def test_resend_confirm_view_returns_200(self):
        response = self.client.post(reverse('resend_confirm'), {'email': self.signup_payload['email']})

        self.assertEqual(response.status_code, 200)

    def test_resend_confirm_email_validation(self):
        response = self.client.post(reverse('resend_confirm'), {'email': 'user2@test.com'})

        self.assertEqual(response.status_code, 400)

    def test_resend_confirm_sends_confirmation_email(self):
        initial_mails_count = len(mail.outbox)

        self.client.post(reverse('resend_confirm'), {'email': self.signup_payload['email']})

        self.assertEqual(len(mail.outbox), initial_mails_count + 1)
        self.assertEqual(mail.outbox[initial_mails_count].subject, 'تأكيد الحساب')


class LoginTestCase(APITestCase):
    def setUp(self):
        self.signup_payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password': 'test1234',
            'first_name': 'Test User'
        }

        self.user = User.objects.create_user(**self.signup_payload)
        self.email = self.user.email_addresses.get(primary=True)
        self.email.verified = True
        self.email.save()

    def test_login_with_username(self):
        # username is case sensitive
        response = self.client.post(reverse('login'), {
            'username': self.signup_payload['username'],
            'password': self.signup_payload['password']
        })

        upper_response = self.client.post(reverse('login'), {
            'username': self.signup_payload['username'].upper(),
            'password': self.signup_payload['password']
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(upper_response.status_code, 400)

    def test_login_with_email(self):
        # email is case insensitive
        response = self.client.post(reverse('login'), {
            'email': self.signup_payload['email'],
            'password': self.signup_payload['password']
        })

        upper_response = self.client.post(reverse('login'), {
            'email': self.signup_payload['email'].upper(),
            'password': self.signup_payload['password']
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(upper_response.status_code, 200)

    def test_login_view_returns_token_with_user_details(self):
        response_data = TokenSerializer(instance=self.user.auth_token).data
        response = self.client.post(reverse('login'), {
            'email': self.signup_payload['email'],
            'password': self.signup_payload['password']
        })

        self.assertEqual(response_data, response.data)


    def test_login_with_unverified_email(self):
        self.email.verified = False
        self.email.save()

        response = self.client.post(reverse('login'), {
            'email': self.signup_payload['email'],
            'password': self.signup_payload['password']
        })

        self.assertEqual(response.status_code, 403)

    def test_login_with_inactive_user(self):
        self.user.is_active = False
        self.user.save()

        response = self.client.post(reverse('login'), {
            'email': self.signup_payload['email'],
            'password': self.signup_payload['password']
        })

        self.assertEqual(response.status_code, 400)

    def test_login_credentials_validation(self):
        responses = []

        # no username nor email
        responses.append(self.client.post(reverse('login'), {
            'password': self.signup_payload['password']
        }))

        # bad email
        responses.append(self.client.post(reverse('login'), {
            'email': 'user2@test.com',
            'password': self.signup_payload['password']
        }))

        # bad username
        responses.append(self.client.post(reverse('login'), {
            'username': 'user2',
            'password': self.signup_payload['password']
        }))

        # bad password
        responses.append(self.client.post(reverse('login'), {
            'email': self.signup_payload['email'],
            'password': 'test12345'
        }))

        for response in responses:
            self.assertEqual(response.status_code, 400)


class LogoutTestCase(APITestCase):
    def setUp(self):
        self.signup_payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password': 'test1234',
            'first_name': 'Test User'
        }

        self.user = User.objects.create_user(**self.signup_payload)

        self.client.login(
            email=self.signup_payload['email'],
            password=self.signup_payload['password']
        )

    def test_logout_view_requires_authentication(self):
        unauthenticated_client = self.client_class()
        response = unauthenticated_client.post(reverse('logout'))

        self.assertEqual(response.status_code, 403)

    def test_logout_view_returns_200(self):
        response = self.client.post(reverse('logout'))

        self.assertEqual(response.status_code, 200)

    def test_logout_view_deletes_token(self):
        self.client.post(reverse('logout'))

        result = Token.objects.filter(user__username=self.signup_payload['username']).exists()

        self.assertFalse(result)


class UserDetailsTestCase(APITestCase):

    def setUp(self):
        self.signup_payload = {
            'username': 'user',
            'email': 'user@test.com',
            'password': 'test1234',
            'first_name': 'Test User'
        }

        self.user = User.objects.create_user(**self.signup_payload)

        self.client.login(
            email=self.signup_payload['email'],
            password=self.signup_payload['password']
        )

    def test_user_details_view_requires_authentication(self):
        unauthenticated_client = self.client_class()
        response = unauthenticated_client.get(reverse('user_details'))

        self.assertEqual(response.status_code, 403)

    def test_user_details_view_returns_user(self):
        response_data = UserDetailsSerializer(instance=self.user).data

        response = self.client.get(reverse('user_details'))

        self.assertEqual(response.data, response_data)

    def test_user_details_fields(self):
        fields = ['username', 'email', 'name',
                  'account', 'avatar_url', 'batch_status']

        response = self.client.get(reverse('user_details'))

        for field in fields:
            self.assertTrue(response.data.__contains__(field))

    def test_user_details_account_fields(self):
        fields = ['last_opened_lesson', 'last_opened_lesson_slug',
                  'last_opened_module_slug', 'last_opened_workshop_slug', 'track']

        response = self.client.get(reverse('user_details'))

        for field in fields:
            self.assertTrue(response.data['account'].__contains__(field))
