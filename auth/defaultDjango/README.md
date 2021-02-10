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

