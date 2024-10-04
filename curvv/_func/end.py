def end(*args):
  import time
  if len(args) == 0:
    trash = input() 
    quit()
  elif len(args) == 1:
    time.sleep(float(args[0]))
    quit()
  else:
    print("ERROR")
