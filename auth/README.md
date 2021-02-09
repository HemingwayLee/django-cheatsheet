# DefaultUser
* use sqlite3
* show default `auth_user` table schema (and data) by a raw SQL query

```
sqlite> .tables
auth_group                  auth_user_user_permissions
auth_group_permissions      django_admin_log          
auth_permission             django_content_type       
auth_user                   django_migrations         
auth_user_groups            django_session
```

```javascript
[{
    "id": 1,
    "password": "pbkdf2_sha256$120000$8G6jXXFYq4sx$NES6L127peQ66opUzouwApWIB1Le1ImS9tBVOmbCHRo=",
    "last_login": null,
    "is_superuser": true,
    "username": "root",
    "first_name": "",
    "email": "root@jp.abc.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2020-06-08T06:44:59.110",
    "last_name": ""
}]
```

# RewriteUser
* use psql
* rewrite `user model` (it is `main_myuser` in this example) and show it by a raw SQL query

```
                 List of relations
 Schema |          Name          | Type  |  Owner   
--------+------------------------+-------+----------
 public | auth_group             | table | Rosemary
 public | auth_group_permissions | table | Rosemary
 public | auth_permission        | table | Rosemary
 public | django_admin_log       | table | Rosemary
 public | django_content_type    | table | Rosemary
 public | django_migrations      | table | Rosemary
 public | django_session         | table | Rosemary
 public | main_myuser            | table | Rosemary
(8 rows)
```

```javascript
[{
	"id": 1,
	"password": "pbkdf2_sha256$120000$pUEcvklDV0tc$6KTTxCKlpvi4woQzTw0GuASlBh+CgtgOgLxxGsFZ+Y4=",
	"last_login": null,
	"email": "abc@gmail.com",
	"date_of_birth": "1985-04-14",
	"is_active": true,
	"is_admin": false
}]
```

# ExtendUser
* use psql
* extend `user model` (it is `main_myuser` in this example) with a new column `age` and show it by a raw SQL query

```
                    List of relations
 Schema |             Name             | Type  |  Owner   
--------+------------------------------+-------+----------
 public | auth_group                   | table | Rosemary
 public | auth_group_permissions       | table | Rosemary
 public | auth_permission              | table | Rosemary
 public | django_admin_log             | table | Rosemary
 public | django_content_type          | table | Rosemary
 public | django_migrations            | table | Rosemary
 public | django_session               | table | Rosemary
 public | main_myuser                  | table | Rosemary
 public | main_myuser_groups           | table | Rosemary
 public | main_myuser_user_permissions | table | Rosemary
(10 rows)
```

```javascript
[{
	"id": 1,
	"password": "pbkdf2_sha256$120000$dK0ZIkUyNiSc$u7xPX5YobEIy8cHcXWSakiPXtRaoI3gOdBKWyJaZ/nU=",
	"last_login": null,
	"is_superuser": true,
	"username": "root",
	"first_name": "",
	"last_name": "",
	"email": "root@abc.com",
	"is_staff": true,
	"is_active": true,
	"date_joined": "2020-06-08T07:17:44.931Z",
	"age": null
}]
```


# formSubmit
![formsubmit1](images/formsubmit1.png)
![formsubmit2](images/formsubmit2.png)
* use sqlite3
* basic login/logout/dashboard functionality with vanilla Django with better UI
* use form submit in frontend
* access control
```python
def hello(request):
    if request.user.is_authenticated: 
        return render(request, 'hello.html')
    else:
        return render(request, 'form_template.html')
```

# customCmsPage
![customCmsPage1](images/customcmspage1.png)
![customCmsPage1](images/customcmspage2.png)
* use psql
* most basic login/logout/dashboard functionality with vanilla Django
* use `LoginView.as_view`
* the `admin` page is not accessible by removing `admin/` from `url.py` 


# cookieBasedAuth
![cookiebasedauth1](images/cookiebasedauth1.png)
![cookiebasedauth2](images/cookiebasedauth2.png)
* use sqlite3
* use jQuery/Bootstarp/Django base template in frontend
* access control
```python
@require_http_methods(["GET"])
@login_required(login_url='/signin/')
def hello(request):
    return render(request, "hello.html")
```

* In `settings.py`
```python
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_AGE = 60
```

# loginLimit
* use sqlite3
* use django-axes

# djangoRest
## helloDjangoRest

