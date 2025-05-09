
import os
import json

def load_json(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as file:
        return json.load(file)

def save_json(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
