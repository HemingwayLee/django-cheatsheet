import sys
from django.apps import AppConfig

class BgConfig(AppConfig):
    name = 'bg'

    def ready(self):
        if 'do_init' in sys.argv:
            print('Doing initialization with new command...')
            
            from background_task.models import Task
            from .task import the_init_task

            tasks = Task.objects.filter(task_name="bg.task.the_init_task")
            if tasks.exists():
                print("exist, not doing anything...")
            else:
                print("not exist, create it...")
                the_init_task(repeat=10, repeat_until=None)
            
            print('Done initialization with new command !!')
