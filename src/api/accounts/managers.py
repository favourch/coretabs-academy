from django.db import models


class EmailAddressManager(models.Manager):

    def add_email(self, user, email):
        email_address, created = self.get_or_create(
            user=user, email__iexact=email, defaults={"email": email}
        )

        email_address.send_confirmation()
        return email_address

    def get_primary(self, user):
        try:
            return self.get(user=user, primary=True)
        except self.model.DoesNotExist:
            return None
