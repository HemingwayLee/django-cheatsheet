
# Setup locally
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

# Setup by docker
```
docker-compose -f docker-compose-psql.yml up
docker-compose -f docker-compose-sqlite3.yml up 
```

