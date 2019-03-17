import pytz
from datetime import datetime, timedelta
from rest_framework.authtoken.models import Token
from django.conf import settings

class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', None)
        # print(token)
        
        if token is not None:
            dbToken = Token.objects.filter(key=token.split(" ")[1])
            if dbToken.count() != 0:
                created = dbToken.first().created
                # print("created: ", created)

                utc_now = datetime.utcnow()
                utc_now = utc_now.replace(tzinfo=pytz.utc)
                # print("now: ", utc_now)

                delta = utc_now - created
                print(delta)

                if delta > timedelta(minutes=settings.EXPIRATION_IN_MIN):
                    print("expired!! signout!!")
                    dbToken.delete()
                else:
                    print("OK, extend you")
                    dbToken.update(created = utc_now)

        return self.get_response(request)
