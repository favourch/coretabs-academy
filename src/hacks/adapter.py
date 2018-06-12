from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpResponseRedirect
from django.shortcuts import reverse


class MyAccountAdapter(DefaultAccountAdapter):

    def respond_email_verification_sent(self, request, user):
        return HttpResponseRedirect('')

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = "/confirm-account/{}".format(emailconfirmation.key)
        ret = request.build_absolute_uri(url)
        return ret
