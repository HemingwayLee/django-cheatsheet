import sys
from time import sleep
from background_task import background

def doPreprocessing():
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def doOcr():
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def annotate():
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

def finish():
    print(f"process in the background... {sys._getframe().f_code.co_name}")
    sleep(8)

@background(schedule=10)
def uploadInBackground(message):
    doPreprocessing()
    doOcr()
    annotate()
    finish()
