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
    "client-package-download-error": {"errorCall":"ClientPackageInstallationError", "description": f"Could not install {singleQuote}{args[1]}{singleQuote}"},
    "wait-command-error": {"errorCall": "WaitTimeCommandError", "description": f"No logic for {singleQuote}{args[1]}{singleQuote}"},
    "end-logic-error": {"errorCall": "EndCommandLogicError", "description": f"Required only 1 argument got {args[1]}"}
  }
  print(errorCodeList[args[0]]["errorCall"] + ": " + errorCodeList[args[0]]["description"])
  quit()
  
def q_m():
  print("\n\n\n\nStill under Production!\n\n\n\n")
  quit()

def repoCreate(token=None, repoName=None, repoType=None):
  print(f"{token} {repoName} {repoType}")
  import os
  apiToken = os.getenv("GITHUB_API")
  if token is None and repoName is None and repoType is None:
    
    q_m()
  elif repoName is not None and repoType is None:
    repoName = repoName
    repoType = "public"
    if token is None:
      if apiToken is None or apiToken == "":
        print("TokenNotFoundError: Please provide a valid token.")
        quit()
      else:
        token = apiToken
    else:
      token = token
    
  elif repoName is not None and repoType is not None:
    repoName = repoName
    repoType = repoType
    if token is None:
      if apiToken is None or apiToken == "":
        print("TokenNotFoundError: Please provide a valid token.")
        quit()
      else:
        token = apiToken
    elif token is not None:
      token = token
  elif repoName is None:
    q_m()
  
  
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
  parser.add_argument(
    "commandCall",
    help="curvv function you want to run"
    )
  parser.add_argument(
    "-tk",
    "--token",
    help="provide token for function",
    metavar="TOKEN",
    dest="token"
    )
  parser.add_argument(
    "-n",
    "--name",
    help="name of repository",
    metavar="REPO_NAME",
    dest="repoName"
    )
  parser.add_argument(
    "--type",
    help="type of repository",
    metavar="TYPE",
    dest="repoType"
    )
  
  args = parser.parse_args()
  command = args.commandCall
  commandList = ["gh-new"]
  
  if command == commandList[0]:
    repoCreate(token=args.token, repoName=args.repoName, repoType=args.repoType)