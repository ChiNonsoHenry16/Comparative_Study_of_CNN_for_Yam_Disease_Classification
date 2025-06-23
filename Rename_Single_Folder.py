# small python codes to rename the new MD folder

import os

# Your folders
folders = [
    r"C:\Users\explo\Downloads\NewMD_6000 - Copy\train",
    r"C:\Users\explo\Downloads\NewMD_6000 - Copy\val",
    r"C:\Users\explo\Downloads\NewMD_6000 - Copy\test"
]

# For each folder: use a temp name first, then final name
for folder_path in folders:
    print(f"\n Processing: {folder_path}")

    files = [f for f in os.listdir(folder_path) if f.lower().endswith(".jpg")]
    files.sort()

    # First rename to a temp name to avoid clashes
    for idx, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)
        temp_name = f"TEMP_RENAME_{idx}.jpg"
        temp_path = os.path.join(folder_path, temp_name)
        os.rename(old_path, temp_path)

    # Then rename temp names to final names
    temp_files = [f for f in os.listdir(folder_path) if f.startswith("TEMP_RENAME_")]
    temp_files.sort()

    for idx, temp_filename in enumerate(temp_files, start=1):
        temp_path = os.path.join(folder_path, temp_filename)
        final_name = f"IMG_{idx}.jpg"
        final_path = os.path.join(folder_path, final_name)
        os.rename(temp_path, final_path)
        print(f"Renamed: {temp_filename} ➡️ {final_name}")

print("\n Done! All images in all folders renamed safely.")
