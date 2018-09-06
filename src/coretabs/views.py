from django.http.response import HttpResponse


def health(request):
    return HttpResponse("OK")
