import sys
import string
import random
from time import sleep
from background_task import background
from .models import MyTask, MyReport

def _id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def doPreprocessing(filename, task):
    task.status = 1
    task.save()

    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(3)

def doOcr(filename, task):
    task.status = 2
    task.save()

    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(3)

def annotate(filename, task):
    task.status = 3
    task.save()
    
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(3)

def finish(filename, task):
    task.status = 4
    task.save()
    
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(3)

@background(schedule=10, queue='do_task')
def uploadInBackground(filename):
    task = MyTask.objects.filter(filename=filename).first()
    if task is not None:
        doPreprocessing(filename, task)
        doOcr(filename, task)
        annotate(filename, task)
        finish(filename, task)
    else:
        print("unexpected error!!!")


@background(schedule=10, queue='time_report')
def doReport():
    filename = _id_generator()
    mr = MyReport(filename=filename)
    mr.save()

    

