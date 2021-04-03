import sys
from time import sleep
from background_task import background
from .models import MyTask

def doPreprocessing(filename, task):
    task.status = 1
    task.save()

    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def doOcr(filename, task):
    task.status = 2
    task.save()

    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def annotate(filename, task):
    task.status = 3
    task.save()
    
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def finish(filename, task):
    task.status = 4
    task.save()
    
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

@background(schedule=10)
def uploadInBackground(filename):
    task = MyTask.objects.filter(filename=filename).first()
    if task is not None:
        doPreprocessing(filename, task)
        doOcr(filename, task)
        annotate(filename, task)
        finish(filename, task)
    else:
        print("unexpected error!!!")
