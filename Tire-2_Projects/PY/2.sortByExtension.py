import os
import shutil
# Set the directory path
directory = "C:/Users/uniqu/OneDrive/Desktop/Being-An-Engineer-/Tire-2_Projects/"

# List all files and directories in the specified path
files = os.listdir(directory)


for file in files:
    if os.path.isfile(os.path.join(directory,file)):#Ignore folder
        extension = os.path.splitext(file)[1][1:] #get the extension 
        print(f"File: {file} | Extension: {extension}")
        
        
        if extension:
            folder_path = os.path.join(directory,extension.upper())
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))
            print(f"Moved: {file} ->  {folder_path}")

                
            print(f"Folder Created: {folder_path}")
