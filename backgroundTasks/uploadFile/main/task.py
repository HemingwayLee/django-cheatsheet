from background_task import background

@background(schedule=10)
def uploadInBackground(message):
    print(f"in the background... {message}")
