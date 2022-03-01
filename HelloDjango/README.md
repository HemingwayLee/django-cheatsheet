# Project created by default

## Prerequisite
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Create a `HelloDjango` directory in your current directory
```
django-admin startproject HelloDjango
```

## Run server

```
python manage.py runserver
```

```
python manage.py help
```

## Project folder structure
```
|-- db.sqlite3
|-- manage.py
`-- mysite
    |-- __init__.py
    |-- asgi.py
    |-- settings.py
    |-- urls.py
    `-- wsgi.py
```

`__init__.py` is just for python, treat this folder as package

