import json
import os

def load_credentials():
        base_dir = os.path.dirname(os.path.dirname(__file__))   # go up from utils → PythonFramework
        file_path = os.path.join(base_dir, "Data", "creds.json")

        with open(file_path, "r") as f:
            return json.load(f)
