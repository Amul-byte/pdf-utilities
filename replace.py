import os
import shutil

path = "/Users/amulpoudel/Desktop/Codes/PYTHN/folder"

try:
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)
    print("Successfully removed:", path)
except PermissionError:
    print("Permission denied. Please check file permissions.")
except FileNotFoundError:
    print("File or directory not found:", path)
except Exception as e:
    print("An error occurred:", e)
