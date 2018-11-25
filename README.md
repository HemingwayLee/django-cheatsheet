# Start project

This will create a `HelloDjango` directory in your current directory
```
django-admin startproject HelloDjango
```

# The development server

```
python manage.py runserver
```

```
python manage.py help
```

# Django is `MVT` framework

* It takes care of the Controller part (Software Code that controls the interactions between the Model and View)

* It leaves us with the template. The template is a HTML file mixed with Django Template Language (DTL)

* We provide the Model, the view and the template then just maps it to a URL

# Django comes with a lightweight web server. Do not use it in production environment

* Security reasons
* It is single thread

https://stackoverflow.com/questions/4867793/using-djangos-built-in-web-server-in-a-production-environment

# Project folder structure
```
myproject/
   manage.py
   myproject/
      __init__.py
      settings.py
      urls.py
      wsgi.py
```

`__init__.py` is just for python, treat this folder as package

## Don't commit `migrations` folder to git
* it will create conflicts
* just run `python manage.py makemigrations` and `python manage.py migrate` on the server


