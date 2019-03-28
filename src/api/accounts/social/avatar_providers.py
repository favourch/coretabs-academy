

class SocialAvatarProvider(object):

    @classmethod
    def get_avatar_url(self, user, size):
        for social_auth in user.social_auths.all():
            if social_auth.avatar_url:
                return social_auth.avatar_url
