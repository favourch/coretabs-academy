import base64
import hmac
import hashlib
import requests

from urllib import parse

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.conf import settings

from rest_framework import status


@login_required
def sso(request):
    payload = request.GET.get('sso')
    signature = request.GET.get('sig')

    if payload is None or signature is None:
        return HttpResponseBadRequest('No SSO payload or signature. Please contact support if this problem persists.')

    # Validate the payload

    try:
        payload = bytes(parse.unquote(payload), encoding='utf-8')
        decoded = base64.b64decode(payload).decode('utf-8')
        assert 'nonce' in decoded
        assert len(payload) > 0
    except AssertionError:
        return HttpResponseBadRequest('Invalid payload. Please contact support if this problem persists.')

    key = bytes(settings.DISCOURSE_SSO_SECRET,
                encoding='utf-8')  # must not be unicode
    h = hmac.new(key, payload, digestmod=hashlib.sha256)
    this_signature = h.hexdigest()

    if not hmac.compare_digest(this_signature, signature):
        return HttpResponseBadRequest('Invalid payload. Please contact support if this problem persists.')

    # Build the return payload

    qs = parse.parse_qs(decoded)
    params = {
        'nonce': qs['nonce'][0],
        'email': request.user.email,
        'external_id': request.user.id,
        'username': request.user.username,
        'name': request.user.first_name
    }

    return_payload = base64.b64encode(bytes(parse.urlencode(params), 'utf-8'))
    h = hmac.new(key, return_payload, digestmod=hashlib.sha256)
    query_string = parse.urlencode(
        {'sso': return_payload, 'sig': h.hexdigest()})

    # Redirect back to Discourse

    url = '%s/session/sso_login' % settings.DISCOURSE_BASE_URL
    return HttpResponseRedirect('%s?%s' % (url, query_string))


@login_required
def notifications(request):

    username = request.user
    discourse_notifications_url = f'{settings.DISCOURSE_BASE_URL}/notifications.json?recent=true&limit=5&api_key={settings.DISCOURSE_API_KEY}&api_username={username}'
    user_notifications = requests.get(discourse_notifications_url)

    if user_notifications.status_code == 200:
        response = JsonResponse(user_notifications.json(), status=status.HTTP_200_OK)
    else:
        response = HttpResponseNotFound()

    return response
