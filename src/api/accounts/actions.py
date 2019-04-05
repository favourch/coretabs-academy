from django import forms
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic.edit import BaseFormView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .utils import render_mail

User = get_user_model()


class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=User.objects.all(),
                                           widget=forms.SelectMultiple())


def send_email(self, request, queryset):
    form = SendEmailForm(initial={'users': queryset})
    return render(request, 'accounts/send_email.html', {'form': form})


class SendUserEmails(BaseFormView):
    template_name = 'accounts/send_email.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('admin:auth_user_changelist')

    def get(self, request):
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        users = form.cleaned_data['users']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        self.send_emails(users, subject, message)
        user_message = f'{users.count()} users emailed successfully!'
        messages.success(self.request, user_message)
        return super(SendUserEmails, self).form_valid(form)

    def send_emails(self, users, subject, message):
        from django.template import Template, Context
        template = Template(message)

        for user in users:
            message_context = {
                'user': user
            }

            c = Context(message_context)
            rendered_message = template.render(c)

            context = {
                'subject': subject,
                'message': rendered_message
            }

            mail = render_mail('accounts/email/email_template', user.email, context)
            mail.send()
