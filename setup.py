import os

# Specify the directory path where you want to create the Python files
directory = os.path.join(os.getcwd())

def create_python_files(directory):
    # Get a list of all the folders in the specified directory
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]

    # Iterate through each folder
    for folder in folders:
        # Extract the number from the folder name
        number = folder[5:]

        # Create the Python file with the corresponding number if it doesn't already exist
        file_path = os.path.join(directory, folder, f's{number}.py')
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass

def fix_python_files_name(directory) :
    # Get a list of all folders in the directory
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    # Rename each folder
    for folder in folders:
        # Check if the folder name starts with "sujet"
        if folder.startswith('sujet'):
            # Extract the number from the folder name
            number = folder.split(' ')[1]
            old_filename = f's {number}.py'
            filename = 's' + str(number) + '.py'
            
            # Rename the folder
            new_file_path = os.path.join(directory, folder, filename)
            if os.path.exists(new_file_path):
                os.remove(os.path.join(directory, folder, old_filename))
            else:
                os.rename(os.path.join(directory, folder, old_filename), new_file_path)

def delete_files_under_10(directory) :
    # Get a list of all folders in the directory
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    # Rename each folder
    for folder in folders:
        # Check if the folder name starts with "sujet"
        if folder.startswith('sujet'):
            # Extract the number from the folder name
            number = folder.split(' ')[1]
            if int(number) < 10 :
                os.remove(os.path.join(directory, folder, f's{number}.py'))

delete_files_under_10(directory)