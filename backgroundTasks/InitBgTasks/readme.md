# How to Run
* Start the server:
```
docker-compose build
docker-compose up
```

# Notes
* Process tasks are inside `init.sh`
* Use `sqlite3` so that the database will still exist after `docker-compose down`
  * we can test the scripts with/without table data exists

