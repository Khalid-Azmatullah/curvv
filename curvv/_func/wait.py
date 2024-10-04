def wait(waitTime):
  import time
  try:
    time.sleep(float(waitTime))
  except:
    print("ERROR")
