from rest_framework.authtoken.models import Token
from django.http import HttpResponseRedirect


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        print(f"my token is {token} !!!")
        print(f"my path is {request.path} !!!")

        if "signin" in request.path:
            return self.get_response(request)

        if token is None:
            return HttpResponseRedirect('/signin/')
        
        return self.get_response(request)

