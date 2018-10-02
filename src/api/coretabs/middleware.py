from django.utils import translation
from coretabs import settings


class AdminLocaleMiddleware:

    def __init__(self, process_request):
        self.process_request = process_request

    def __call__(self, request):

        if request.path.startswith('/admin'):
            translation.activate("en")

        else:
            translation.activate("ar")

        request.LANGUAGE_CODE = translation.get_language()
        response = self.process_request(request)

        return response


class CrossDomainSessionMiddleware:

    def __init__(self, process_request):
        self.process_request = process_request

    def __call__(self, request):
        response = self.process_request(request)
        if response.cookies:
            try:
                host = request.META['HTTP_ORIGIN']
                # check if it's a different domain
                if host in settings.COOKIE_DOMAINS:
                    for cookie in response.cookies:
                        if cookie == 'csrftoken' or cookie == 'sessionid':
                            response.cookies[cookie]['domain'] = settings.COOKIE_DOMAINS[host]
            except KeyError:
                pass

        return response
