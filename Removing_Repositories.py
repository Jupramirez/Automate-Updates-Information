#!/usr/bin/env python3

import requests
from dotenv import load_dotenv
import os

# 1. Your configuration
load_dotenv()  # Load environment variables from .env file 
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Make sure to set this in your .env file
USERNAME = 'Jupramirez'
# Add the names of the repos you want to delete here
REPOS_TO_DELETE = [
    'Blog-with-Flask'
]

# If True, it actually deletes. If False, it only prints what it would do.
delete_mode = True 

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

for repo in REPOS_TO_DELETE:
    url = f'https://api.github.com/repos/{USERNAME}/{repo}'
    
    if delete_mode:
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            print(f"✅ Successfully deleted: {repo}")
        else:
            print(f"❌ Failed to delete {repo}: {response.json().get('message')}")
    else:
        print(f"👀 DRY RUN: Would delete {repo}")