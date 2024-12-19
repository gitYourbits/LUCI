import os
import time
import sys
import requests

from .state import State
state_instance = State()

from .controller.main import open_vscode
from .controller.llm import llm_response
from .watcher.main import watch_and_update

def luci_start():
    """Start the LUCI session and display a fancy design."""
    if state_instance.is_active():
        print("LUCI is already active.")
        return

    state_instance.activate()
    print("""
    ██╗     ██╗   ██╗ ██████╗██╗
    ██║     ██║   ██║██╔════╝██║
    ██║     ██║   ██║██║     ██║
    ██║     ██║   ██║██║     ██║
    ███████╗╚██████╔╝╚██████╗██║
    ╚══════╝ ╚═════╝  ╚═════╝╚═╝
         ....LUCI is running now!""")


def luci_end():
    """End the LUCI session."""
    if not state_instance.is_active():
        print("LUCI is not active.")
        return

    state_instance.deactivate()
    print("LUCI session ended. Goodbye!")

def get_project_path():
    """Ask the user for the project path interactively."""
    project_name = input("Please enter the name of the project you want to open: ").strip()

    print("Searching for Project...")
    response = requests.post(
        "http://localhost:8000/api/controller/open/",  # Replace with actual API endpoint
        json={"projectName": project_name}
    )

    if response.status_code == 200:
        project_path = response.json().get('projectPath')  # Extract project path from the response

        if project_path:
            print(f"Found project at: {project_path}")
            print("Opening VS Code...")
            open_vscode(project_path)
            return project_path
    elif response.status_code == 404:
        print("Project not found. Do you want to create a new one?")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def get_llm_response():
    """Get responses from LLM for user prompts."""
    while True:
        prompt = input("Run 'deactivate' to deactivate LLM mode\n")
        if prompt == 'deactivate':
            return 'deactivate'
        try:
            response = llm_response(prompt)
            return response
        except Exception as e:
            print(e)
            print("Could not connect to remote LLM. Try later...")

def handle_command(command, *args):
    """Handle user commands based on LUCI state."""
    if command == "start":
        luci_start()
    elif command == "end":
        luci_end()
    elif not state_instance.is_active():
        print("LUCI is inactive. Try running 'luci start'.")
    elif command == "create":
        print("Watching project files...")
        project_path = args[0] if args else input("Enter project path: ").strip()
        watch_and_update(project_path, "http://localhost:8000/api/memory/update/")
    elif command == "open":
        get_project_path()
    elif command == "activate":
        print("Welcome to LUCI LLM mode!\n Write a Prompt...\n")
        while True:
            response = get_llm_response()
            if response == 'deactivate':
                print("Switching to cli mode.")
                break
            else:
                print(response)
            time.sleep(1)  # Brief pause before prompting again
    elif command == '--help':
        print("""   
Available Commands:
    start           Start luci
    create          Create a new project
    open            Open existing project
    activate        Activate a model
    end             Stop luci

Flags:
    -h, --help      help for luci
        """)
    else:
        print(f"Unknown command: {command}")

def main():
    """Entry point for the LUCI CLI."""
    if len(sys.argv) < 2:
        print("Usage: luci <command> [options]")
        return

    command = sys.argv[1]
    args = sys.argv[2:]
    handle_command(command, *args)


if __name__ == "__main__":
    main()
