

def get_social_auth(uid, provider):
    from .models import UserSocialAuth

    try:
        social_auth = UserSocialAuth.objects.get(uid=uid, provider=provider)
    except UserSocialAuth.DoesNotExist:
        social_auth = None

    return social_auth


def get_user_by_email(email):
    from .models import User

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        user = None

    return user


def create_user_social(data):
    from .models import User

    username = clean_username(data['username'])
    email = data['email']
    password = User().set_unusable_password()
    first_name = data['name']

    user = User.objects.create_user(username, email, password, first_name=first_name)
    user.email_addresses.get(primary=True).confirm()

    return user


def clean_username(username):
    from .models import User
    i = 1

    while User.objects.filter(username=username).exists():
        username = f'{username}{i}'
        i += 1

    return username


def create_social_auth(user, uid, provider):
    from .models import UserSocialAuth

    social_auth = UserSocialAuth.objects.create(user=user, provider=provider, uid=uid)

    return social_auth
