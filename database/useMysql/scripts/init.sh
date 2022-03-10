#!/bin/bash

while ! mysqladmin ping -h "$MYSQL_HOST" --silent; do
    >&2 echo "wait for MySQL..."
    sleep 3
done

>&2 echo "MySQL is up"

pwd
ls

cd /home/proj/
python3 manage.py makemigrations myapp
python3 manage.py migrate

>&2 echo "Superuser NOT Exist!!! This is fresh install mode"
  
cd /home/proj/scripts/
./create_superuser.sh

cd /home/proj/
python3 manage.py runserver 0.0.0.0:8000

