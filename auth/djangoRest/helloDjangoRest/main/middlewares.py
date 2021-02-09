from rest_framework.authtoken.models import Token

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        print(f"my token is {token} !!!")
        
        return self.get_response(request)
