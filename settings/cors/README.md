

# Setup
## backend
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```

## frontend
```
npm install 
npm start 
```

# Explain
Test cors problem

## Details
```
pip3 install django-cors-headers
```

and then add it to `settings.py`:

```python
INSTALLED_APPS = (
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',  
    'django.middleware.common.CommonMiddleware',  
)

CORS_ORIGIN_ALLOW_ALL = True
```

Or

```python
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3030',
]
```

