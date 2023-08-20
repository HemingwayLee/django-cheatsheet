#!/bin/bash

pwd
ls

cd /home/proj/
python3 manage.py makemigrations myapp
python3 manage.py migrate

COUNT=$(sqlite3 "db.sqlite3" "select count(*) from auth_user;")

echo $COUNT

# COUNT=$(PGPASSWORD=${POSTGRES_PASSWORD} psql -h ${POSTGRES_HOST} -p 5432 -U postgres -d ${POSTGRES_DB_NAME} -tAc 'select count(*) from auth_user;')
if [ "$COUNT" -gt "0" ] ; then
  >&2 echo "Superuser Exist!!! This is hotfix mode"
  >&2 echo "No need to create superuser"
else
  >&2 echo "Superuser NOT Exist!!! This is fresh install mode"
  cd /home/proj/scripts/
  ./create_superuser.sh
fi


cd /home/proj/
python3 manage.py runserver 0.0.0.0:8000
