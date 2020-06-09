from django.contrib.auth.models import User
from rest_framework import viewsets, serializers
from rest_auth.views import LoginView

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Only successful login will invoke the following functions
class CustomLoginView(LoginView):
    def login(self):
        print("inside login")
        super().login()

    def get_response(self):
        print("inside get_response")

        orginal_response = super().get_response()
        mydata = { "hello": "word", "yes": "man" }
        orginal_response.data.update(mydata)
        
        return orginal_response

