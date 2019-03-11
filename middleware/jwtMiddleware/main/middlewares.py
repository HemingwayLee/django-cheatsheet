from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import User
from django.contrib.auth.middleware import get_user
from django.http import HttpResponse, JsonResponse
import jwt
import json

class JwtMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == "/auth/signin/":
            return self.get_response(request)
        
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))
        if not request.user:
            return JsonResponse({"detail": "This action is not authorized"})

        return self.get_response(request)

    @staticmethod
    def get_jwt_user(request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        user = None
        if token is not None:
            try:
                jwt = jwt.decode(
                    token,
                    django.conf.settings.SECRET_KEY,
                    algorithms=['HS256'])
                
                user = User.objects.get(id=jwt['user_id'])
            except Exception as e:
                print("incorrect token")
        
        return user
