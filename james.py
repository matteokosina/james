#!/usr/bin/env python3

import os
import shutil
import subprocess


repo = None
target_service = None
commands = []



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
        


def read_james_file(file_path='james.txt'):
    try:
        with open(file_path, 'r') as file:
            # Read the file line by line
            lines = file.readlines()

            # Extract repo and target_service from the first two lines
            if lines:
                repo = lines[0].strip()

            if len(lines) > 1:
                target_service = lines[1].strip()

            # Add the rest of the lines to the commands array
            commands = [line.strip() for line in lines[2:]]

            print(f"Orders from menu {file_path} have been processed.")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error: {e}")
    return repo, target_service, commands
   
        


def run_commands(commands):
    try:
        for command in commands:
            # Run each command using subprocess
            subprocess.run(command, shell=True)
            print("job: ", command, " started")
    except Exception as e:
        print(f"Error: {e}")
      
    print("Thank you for your visit - james")
        

if __name__ == "__main__":
    repo, target_service, commands = read_james_file('james.txt')
    print("Update-repo:", repo)
    print("Target Service:", target_service)
    clean_and_clone_repo(target_service, repo)
    run_commands(commands)
