

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

    user = User.objects.create_user(data['username'], data['email'],
                                    User().set_unusable_password(), first_name=data['name'])

    user.email_addresses.get(primary=True).confirm()

    return user


def create_social_auth(user, uid, provider):
    from .models import UserSocialAuth

    social_auth = UserSocialAuth.objects.create(user=user, provider=provider, uid=uid)

    return social_auth


def retrieve_username_from_email(email):
    pass
