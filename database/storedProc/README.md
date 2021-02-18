

# Setup
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
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

# Test it with `grafana`
```
docker-compose build
docker-compose up
```

* Access `127.0.0.1:3000`
  * default account/pwd is `admin/admin`
  * Add postgres connection with `mydb:5432`
  * Add postgres to panel
  * Create queries

