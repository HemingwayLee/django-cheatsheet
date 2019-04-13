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

# Tips

## Extend `users` model
https://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django

## Connection pool  
By default, the connection pool is off in Django.

# Todo
## class based views
https://stackoverflow.com/questions/17414622/django-a-good-tutorial-for-class-based-views

## class vs function in view  
https://stackoverflow.com/questions/14788181/class-based-views-vs-function-based-views

## middleware 

## limit and offset in Django is different  
https://stackoverflow.com/questions/24041448/specifying-limit-and-offset-in-django-queryset-wont-work
