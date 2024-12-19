import os
import time
import requests
from controller.main import *

def get_project_path():
    """Ask the user for the project path interactively."""
    while True:
        project_path = input("Please enter the path to the project directory: ").strip()
        if os.path.isdir(project_path):  # Check if the directory exists
            return project_path
        else:
            print("The provided path is invalid. Please try again.")

def ask_for_action():
    """Prompt the user for the action they want to perform."""
    while True:
        action = input("What would you like to do? (watch/open/exit): ").strip().lower()
        if action in ['watch', 'open', 'exit']:
            return action
        else:
            print("Invalid choice. Please choose 'watch', 'open', or 'exit'.")

def main():
    print("Welcome to LUCI CLI Tool!")

    # Step 1: Get project path from user
    project_path = get_project_path()

    while True:
        # Step 2: Ask user what action they want to perform
        action = ask_for_action()

        if action == 'watch':
            print("Watching and extracting project files...")
            response = requests.post(
                "http://localhost:8000/api/memory/update/",  # Replace with actual API endpoint
                json={"project_path": project_path}
            )
            if response.status_code == 200:
                print("Project files are being watched and updated.")
            else:
                print(f"Error: {response.status_code} - {response.text}")

        elif action == 'open':
            print("Opening project in VS Code...")
            open_vscode(project_path)

        elif action == 'exit':
            print("Exiting the LUCI CLI tool. Goodbye!")
            break

        # Wait before prompting for the next action
        time.sleep(1)

if __name__ == "__main__":
    main()
