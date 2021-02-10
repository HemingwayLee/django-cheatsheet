#!/bin/bash

USER="ywlee"
PASS="pwd"
MAIL="ywlee@jp.abc.com"
SCRIPT="
from django.contrib.auth.models import User
username = '$USER'
password = '$PASS'
email = '$MAIL'
if User.objects.filter(username=username).count()==0:
  user = User.objects.create_user(username, email, password)  
  user.is_staff=True 
  user.save()
else:
  print('Skip! super user exists...')
"

printf "$SCRIPT" | python3 /home/proj/manage.py shell

