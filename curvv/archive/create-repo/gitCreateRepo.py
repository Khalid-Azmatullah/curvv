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
