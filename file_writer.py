import json
from config_reader import config as cr
import os

directory_path = cr.get('Results', 'directory_path')

def write_data_to_file(filename, json_data):
    """
    Writes JSON data to a file.

    Args:
        filename (str): The name of the file to write to.
        json_data (dict): The JSON data to write.
    """
    try:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing to file: {e}")

# Example usage
# write_data_to_file("example.json", {"key": "value"})
