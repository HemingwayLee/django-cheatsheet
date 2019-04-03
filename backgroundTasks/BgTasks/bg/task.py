from background_task import background

@background(schedule=10)
def demo_task(message):
  print("in the background...".format(message))
