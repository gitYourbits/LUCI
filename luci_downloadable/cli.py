import os
import time
import requests
from controller.main import *

def get_project_path():
    """Ask the user for the project path interactively."""
    projectName = input("Please enter name of the project that you want to open: ").strip()

    print("Searching for Project...")
    response = requests.post(
        "http://localhost:8000/api/vscode/open/",  # Replace with actual API endpoint
        json={"projectName": projectName}
    )

    if response.status_code == 200:
        project_path = response.json().get('projectPath')  # Extract project path from the response

        if project_path:
            print(f"Found project at: {project_path}")
            print("Opening VS Code...")
            open_vscode(project_path)
            return project_path
    elif response.status_code == 404:
        print(f"Error: {response.status_code} - {'Project not found. Do you want to create a new one?'}")


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

    while True:
        # Step 2: Ask user what action they want to perform
        action = ask_for_action()

        if action == 'watch':
            print("Watching and extracting project files...")
            response = requests.post(
                "http://localhost:8000/api/memory/update/",  # Replace with actual API endpoint
                json={
                        "projectName": f"{input("Specify the name of your project: ")}",
                        "projectPath": f"{input("Full Path to Project: ")}",
                        "memoryData": {
                            "file1.py": [["1", "import os"]]
                        }
                    }
            )
            if response.status_code == 200:
                print("Project files are being watched and updated.")
            else:
                print(f"Error: {response.status_code} - {response.text}")

        elif action == 'open':
            get_project_path()
                        
        elif action == 'exit':
            print("Exiting the LUCI CLI tool. Goodbye!")
            break

        # Wait before prompting for the next action
        time.sleep(1)

if __name__ == "__main__":
    main()
