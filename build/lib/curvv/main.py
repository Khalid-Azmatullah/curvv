#packages and modules
import time
import random
import sys
import subprocess
import platform
import datetime
import os
singleQuote= "'"

# error function
def errorCode(*args):
  # issues
  errorCodeList = {
    "package-installation-error": {"errorCall":"ExternalPackageInstallationError", "description": "Could not install required package."},
    "client-package-download-error": {"errorCall":"ClientPackageInstallationError", "description": f"Could not install {singleQuote}{args[1]}{singleQuote}"},
    "wait-command-error": {"errorCall": "WaitTimeCommandError", "description": f"No logic for {singleQuote}{args[1]}{singleQuote}"},
    "end-logic-error": {"errorCall": "EndCommandLogicError", "description": f"Required only 1 argument got {args[1]}"}
  }
  print(errorCodeList[args[0]]["errorCall"] + ": " + errorCodeList[args[0]]["description"])
  quit()
  
# downloading external packages
externalPackageRequirements = ["bs4", "requests", "colorama", "rich", "importlib"]
for i in range(len(externalPackageRequirements)):
  try:
    __import__(externalPackageRequirements[i])
  except:
    try:
      subprocess.check_call([sys.executable, "-m", "pip", "install", externalPackageRequirements[i]])
    except:
      errorCode("package-installation-error")

import requests
from bs4 import BeautifulSoup as htmlParser

moduleLibrary = {}
urlForModuleLibrary = "https://docs.python.org/3/py-modindex.html"
response = requests.get(urlForModuleLibrary)
if response.status_code == 200: #ok
    snakeForWebScarping = htmlParser(response.content, "html.parser")
    moduleNameList = snakeForWebScarping.find_all(class_="xref")

    for module in moduleNameList:
      moduleLibrary[module.text] = f"{module.text}"
else:
    print(f"Failed to retrieve module library. Status code: {response.status_code}")


def packageSafety(*args):
  for package in range(len(args)):
    try:
      __import__(args[package])
    except:
      try:
        subprocess.run(
          [sys.executable, '-m', 'pip', 'install', args[package]],
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE
        )
        __import__(args[package])
      except:
        return errorCode("client-package-download-error" ,package)

def end(*args):
  if len(args) == 0:
    trash = input() 
    quit()
  elif len(args) == 1:
    time.sleep(float(args[0]))
    quit()
  else:
    errorCode("end-logic-error", len(args))

def wait(waitTime):
  import time
  try:
    time.sleep(float(waitTime))
  except:
    errorCode("wait-command-error", waitTime)

from pathlib import Path
def clearCache():
    path = Path(".")
    for pycFile in path.rglob("*.pyc"):
        pycFile.unlink()
    for pycacheDir in path.rglob("__pycache__"):
        pycacheDir.rmdir()
