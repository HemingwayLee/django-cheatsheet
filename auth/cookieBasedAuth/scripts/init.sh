#!/bin/bash

pwd
ls

cd /home/proj/
rm db.sqlite3 
python3 manage.py makemigrations main
python3 manage.py migrate

cd /home/proj/scripts/
./create_superuser.sh

cd /home/proj/
python3 manage.py runserver 0.0.0.0:8000
