def packageSafety(*args):
  import subprocess
  import sys
  uninstalledPackages = []
  for package in range(len(args)):
    try:
      
      __import__(args[package])
    except:
      uninstalledPackages.append(args[package])
  try:
    string = ""
    for i in range(len(uninstalledPackages)):
      string = f"{string}, {uninstalledPackages[i]}"
    subprocess.run(
      [sys.executable, "-m", "pip", "install", string],
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE
    )
    __import__(args[package])
  except Exception as e:
    print(e)
    quit()
  return True