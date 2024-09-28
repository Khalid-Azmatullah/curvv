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
externalPackageRequirements = ["bs4", "requests", "colorama", "rich", "importlib", "argparse"]
for i in range(len(externalPackageRequirements)):
  try:
    __import__(externalPackageRequirements[i])
  except:
    try:
      subprocess.check_call([sys.executable, "-m", "pip", "install", externalPackageRequirements[i]])
    except:
      errorCode("package-installation-error")

def importModuleLibrary():
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
          [sys.executable, "-m", "pip", "install", args[package]],
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

def repoCreate(token, repoName, repoType):
  if repoType == "public":
    repoType = "false"
  elif repoType == "private":
    repoType = "true"
  import os
  import subprocess
  
  pythonCode = """
import sys
import requests
import json

# Get arguments from command line
token = sys.argv[1]
repo_name = sys.argv[2]
repo_type = sys.argv[3]

# Function to convert string to boolean
def string_to_boolean(s):
    if isinstance(s, str):
        if s.lower() in ['true', '1']:
            return True
        elif s.lower() in ['false', '0']:
            return False
    return None  # Return None if the string is not recognized

# Convert repo_type to boolean
repo_type = string_to_boolean(repo_type)

# GitHub API URL for creating a repository
url = 'https://api.github.com/user/repos'

# Set up the HTTP request headers
headers = {
    'Authorization': 'token ' + token,
    'User-Agent': 'Python'
}

# Repository data
data = {
    'name': repo_name,
    'description': '',
    'private': repo_type  # Set to True for a private repo
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Handle the response
if response.status_code == 201:  # HTTP Created
    print("Repository created: " + response.json()['html_url'])
else:
    print(f"Error creating repository: " + str(response.status_code) + response.text)
  """
  pythonFile = 'tempScript.py'
  with open(pythonFile, 'w') as file:
      file.write(pythonCode)
  try:
      result = subprocess.run(["python", pythonFile, token, repoName, repoType])
      if result.stderr:
          print("Error while connecting")
          print(result.stderr)
  except Exception as e:
      print(f"Error while connecting: {e}")
  try:
      os.remove(pythonFile)
      print(f"^")
  except Exception as e:
      print(f"Error deleting file: {e}")


import argparse
def runCvvCommands():
  parser = argparse.ArgumentParser(description="Command for running Curvv functions")
  parser.add_argument("arg1", help="Curvv function you want to run.")
  parser.add_argument("arg2", help="Additional Dependencies")
  parser.add_argument("arg3", help="Additional Dependencies")
  parser.add_argument("arg4", help="Additional Dependencies")
  
  args = parser.parse_args()
  command = args.arg1
  commandList = ["repo.new"]
  if command == commandList[0]:
    repoCreate(token=args.arg2, repoName=args.arg3, repoType=args.arg4)