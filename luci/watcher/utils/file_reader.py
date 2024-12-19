import os

def read_project_files(project_path, file_extensions):
    extracted_data = {}
    for root, _, files in os.walk(project_path):
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    extracted_data[file] = [(i + 1, line) for i, line in enumerate(f.readlines())]
    return extracted_data
