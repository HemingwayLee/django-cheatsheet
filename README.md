# How to start

```
django-admin startproject myproject
django-admin startapp myapp

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```


# Django is `MVT` framework

* It takes care of the Controller part (Software Code that controls the interactions between the Model and View)

* It leaves us with the template. The template is a HTML file mixed with Django Template Language (DTL)

* We provide the Model, the view and the template then just maps it to a URL

