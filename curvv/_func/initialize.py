def initialize():
  import subprocess
  # downloading external packages
  externalPackageRequirements = ["bs4", "requests", "colorama", "rich", "importlib", "argparse"]
  for i in range(len(externalPackageRequirements)):
    try:
      __import__(externalPackageRequirements[i])
    except:
      try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", externalPackageRequirements[i]])
      except Exception as e:
        print("ERROR")
        quit()
