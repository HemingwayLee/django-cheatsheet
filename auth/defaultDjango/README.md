# DefaultUser
* use sqlite3
* show default `auth_user` table schema (and data) by a raw SQL query
  * Note: the table will be different in different versions of django

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
	"password": "pbkdf2_sha256$216000$ptiBIBqLef7O$lClMWyagBYI2U3S4hMmXolhl1PT2Y3Yu2Ilj4y4d5QM=",
	"last_login": null,
	"is_superuser": true,
	"username": "root",
	"last_name": "",
	"email": "root@jp.abc.com",
	"is_staff": true,
	"is_active": true,
	"date_joined": "2021-02-10T05:57:18.973",
	"first_name": ""
}, {
	"id": 2,
	"password": "pbkdf2_sha256$216000$qjtrPPqvxteY$0k5U2Hdfho6efWf8fDadJSwCpwAtNu1TkoEEAoy0F/4=",
	"last_login": null,
	"is_superuser": false,
	"username": "ywlee",
	"last_name": "",
	"email": "ywlee@jp.abc.com",
	"is_staff": true,
	"is_active": true,
	"date_joined": "2021-02-10T05:57:20.277",
	"first_name": ""
}, {
	"id": 3,
	"password": "pbkdf2_sha256$216000$g8nwHa4HW4cr$ykel22RKqxxxW2DNT5hcw3FkslNxXK1gII8ZbBj7+AE=",
	"last_login": null,
	"is_superuser": false,
	"username": "ywlee2",
	"last_name": "",
	"email": "ywlee2@jp.abc.com",
	"is_staff": false,
	"is_active": true,
	"date_joined": "2021-02-10T05:57:21.525",
	"first_name": ""
}]
```

* Access `http://127.0.0.1:8000/admin/`
  * superuser can change/add all users
  * stuff can login and change its own password only
  * client can not login

