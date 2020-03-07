

# Setup
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py createsuperuser
python3 manage.py makemigrations myapp
python3 manage.py migrate
python3 manage.py runserver
```

# Put the following settings in the .env file

```
POSTGRES_USER=username
POSTGRES_PWD=pwd
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```

