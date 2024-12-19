import subprocess
import os

def open_vscode(project_path):
    if os.path.exists(project_path):
        subprocess.run(["code", project_path], shell=True)
        return {"status": "success", "message": "VS Code opened."}
    return {"status": "error", "message": "Project path not found."}
