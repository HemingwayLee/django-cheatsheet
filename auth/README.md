# DefaultUser
* use sqlite3
* show table structure by a raw SQL query

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
* rewrite user model and show it by a raw SQL query

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
* extend user model and show it by a raw SQL query

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

# customCmsPage
* use psql
* basic login/logout/dashboard functionality with vanilla Django






