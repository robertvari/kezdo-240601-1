import json, os, time
from PIL import Image

# store the full path to the photo folder
# r = raw string
dir_path = r"D:\Work\PythonSuli\kezdo-240601\photos"

assert os.path.exists(dir_path), f"Folder path does not exist: {dir_path}"
assert os.path.isdir(dir_path), f"Path must be a directory: {dir_path}"

# collect images from dir_path and create the photo_data dictionary
start_time = time.time()

photo_data = {}
for image in os.listdir(dir_path):
    full_path = os.path.join(dir_path, image)
    file_size = os.path.getsize(full_path) / (1024*1024)
    img = Image.open(full_path)
    photo_data[image] = {"pixel_size": img.size, "file_size": file_size}

stop_time = time.time() - start_time
print(f"Process timer: {stop_time}")

with open("photo_data.json", "w") as f:
    json.dump(photo_data, f)