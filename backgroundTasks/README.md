# Get status of Background Tasks

https://stackoverflow.com/questions/46766939/getting-status-of-task-from-django-background-tasks

# Run multiple Background Tasks

```python
@background(queue='my-queue')
def notify_user(user_id):
    print("my queue")
```

If you run the command `process_tasks` with the option `--queue <queue_name>` you can restrict the tasks processed to the given queue.

