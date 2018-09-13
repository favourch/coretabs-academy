from django.contrib.auth.tokens import PasswordResetTokenGenerator


class ApproveUserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk) + str(user.is_approved) + str(timestamp)


approve_user_token_generator = ApproveUserTokenGenerator()
