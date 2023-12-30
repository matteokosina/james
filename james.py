#!/usr/bin/env python3

import os
import shutil
import subprocess

def clean_and_clone_repo(path, git_repo_url):
    try:
        # Remove all contents of the folder
        if os.path.exists(path):
            shutil.rmtree(path)
        
        # Create the folder if it doesn't exist
        os.makedirs(path)

        # Clone the Git repository into the specified folder
        subprocess.run(['git', 'clone', git_repo_url, path])

        print(f"Git repository cloned successfully into {path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
   
    folder_path = '/path/to/your/service'
    git_repository_url = 'url/to/your/update/repo'

    clean_and_clone_repo(folder_path, git_repository_url)
