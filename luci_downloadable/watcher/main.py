from .utils.file_reader import read_project_files
import requests

def watch_and_update(project_path, llm_api_url):
    file_extensions = ['.py', '.html', '.css', '.js', '.txt']
    extracted_data = read_project_files(project_path, file_extensions)

    # Send data to backend memory
    payload = {
        "projectName": os.path.basename(projectName),
        "projectPath": projectPath,
        "memoryData": extracted_data
    }
    response = requests.post(llm_api_url, json=payload)
    return response.json()
