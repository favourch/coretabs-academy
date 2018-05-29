from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.http import HttpResponseRedirect
from django.conf import settings


class MyAccountAdapter(DefaultAccountAdapter):

    def respond_email_verification_sent(self, request, user):
        return HttpResponseRedirect('')

    # def get_email_confirmation_url(self, request, emailconfirmation):
    #     url = 'confirm-email/{}'.format(emailconfirmation.key)
    #     ret = "{}/{}".format(settings.SITE_URL, url)
    #     return ret
