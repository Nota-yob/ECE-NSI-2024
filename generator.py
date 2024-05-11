import os

directory = os.path.join(os.getcwd())

# Get a list of all folders in the directory
folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

# Rename each folder
for folder in folders:
    # Check if the folder name starts with "sujet"
    if folder.startswith('sujet'):
        # Extract the number from the folder name
        number = folder.split(' ')[1]
        
        # Pad the number with leading zeros to make it 2 digits
        new_number = number.zfill(2)
        
        # Construct the new folder name
        new_folder = f'sujet {new_number}'
        
        # Rename the folder
        os.rename(os.path.join(directory, folder), os.path.join(directory, new_folder))