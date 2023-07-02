import os
import json

# THIS FILE WAS GENERATED USING BING AI
# this is just a simple script that indexes all the unindexed textures

current_dir = os.path.dirname(__file__)
paths_dict = {}


def list_files_and_folders(dir):
    for entry in os.scandir(dir):
        path = entry.path
        if path not in paths_dict:
            if entry.is_file() and path.endswith(".png"):
                rel_path = os.path.relpath(path, current_dir)
                rel_path = rel_path.replace("\\", "/")
                paths_dict[rel_path] = {"Animated": False}
            elif entry.is_dir():
                list_files_and_folders(path)


list_files_and_folders("textures")


with open("textures/texture_index.json", "r") as f:
    existing_data = json.load(f)


for key, value in existing_data.items():
    if key in paths_dict:
        paths_dict[key] = value

with open("textures/texture_index.json", "w") as f:
    json.dump(paths_dict, f, indent=4)
