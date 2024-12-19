import os  # For interacting with the operating system (checking for files, etc.)
import json  # For handling JSON data (reading/writing session data)

class State:  # Defines a class to manage the active/inactive state of LUCI
    def __init__(self, state_file="./luci_state.json"):  # Constructor with a default state file
        self.state_file = state_file  # Path to the file storing LUCI's state
        self.state = {"active": False}  # Default state is inactive
        self._load_state()  # Load the state from the file during initialization

    def _load_state(self):  # Private method to load state from the file
        if os.path.exists(self.state_file):  # Check if the state file exists
            with open(self.state_file, "r") as file:  # Open the file in read mode
                self.state = json.load(file)  # Load the state from the JSON file
        else:
            self._save_state()  # If the file doesn't exist, save the default state

    def _save_state(self):  # Private method to save the state to the file
        with open(self.state_file, "w") as file:  # Open the file in write mode
            json.dump(self.state, file)  # Save the state as JSON in the file

    def activate(self):  # Method to activate LUCI
        self.state["active"] = True  # Set the state to active
        self._save_state()  # Save the updated state to the file

    def deactivate(self):  # Method to deactivate LUCI
        self.state["active"] = False  # Set the state to inactive
        self._save_state()  # Save the updated state to the file

    def is_active(self):  # Method to check if LUCI is active
        return self.state["active"]  # Return the value of the active key
