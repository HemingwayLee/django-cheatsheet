import os
import json
from django.contrib.auth.models import User

username = os.environ['DJANGO_USER']
password = os.environ['DJANGO_PASS']
email = "ywlee@gmail.com"

if User.objects.filter(username=username).count() == 0:
    User.objects.create_superuser(username, email, password)
    print('Super user created!')
else:
    print('Skip! super user exists...')

with open('users.json') as f:
    data = json.load(f)
    for ele in data["users"]:
        username = ele['name']
        password = ele['password']
        email = ele['email']
        is_staff = bool(ele['is_staff'])

        if User.objects.filter(username=username).count()== 0:
            User.objects.create_user(username, email, password, is_staff=is_staff)
            print(f'user {username} created!')
        else:
            print(f'Skip! user {username} exists...')
