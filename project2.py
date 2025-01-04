import os
entries = os.listdir('folder')
print(f"Contents of the directory '{'folder'}':")
for entry in entries:
    print(entry)
    if entry.endswith(".png"):
        os.rename(f"folder/{entry}",f"abc.png")
       