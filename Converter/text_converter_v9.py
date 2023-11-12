import os
import shutil
import json
from check_json import JSONReader  # Importing the JSONReader class


# Specify the path to for imported_data 
imported_data = 'insert the directory of the imported_data '  # fill the code here

# Function to find and load the JSON configuration file
def find_and_load_config_file(subfolder_path):
    config_file_path = os.path.join(subfolder_path, 'Configuration.json')
    if os.path.exists(config_file_path):
        with open(config_file_path, 'r') as f:
            config_data = json.load(f)
            return config_data
    else:
        return None

#Read th JSON configuration file,process the data 
#so that i can approach subfolders..
def process_data_from_config(source_folder, gles_folder):
    successful_conversion = False 
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        if os.path.isdir(subfolder_path):
            config_data = find_and_load_config_file(subfolder_path)

            if config_data:
                json_reader = JSONReader(os.path.join(subfolder_path, 'Configuration.json'))
                json_reader.read_json()
                if not json_reader._parse_source_dir() and \
                        json_reader._parse_target_dir() and \
                        json_reader._parse_source_labels() and \
                        json_reader._parse_target_labels() and \
                        json_reader._parse_mapping():
                            print(f"Skipping folder {subfolder} due to JSON errors.")
                            continue

                # Extract data frm json fiel
                source_dir = os.path.join(subfolder_path, 'data')  # Adjust source directory as needed
               
                mapping = config_data["mapping"]

                # Create a new directory within the GLES directory with the specified folder name
                # to be sure about the data and dont mix up data
                new_folder_name = f"{subfolder}_converted" 
                new_destination = os.path.join(gles_folder, new_folder_name)
                os.makedirs(new_destination, exist_ok=True)

                # Listing all files in the source directory (GLES)
                files = os.listdir(source_dir)

                # Copy files to the new folder (so that i dont merge files)
                for file in files:
                    source_file_path = os.path.join(source_dir, file)
                    destination_file_path = os.path.join(new_destination, file)
                    if os.path.isfile(source_file_path):
                        shutil.copy(source_file_path, new_destination)  # Copy files to the new folder

                # Read and write text files in the new folder, updating the keys according to the mapping in the JSON file
                for file in os.listdir(new_destination):
                    file_path = os.path.join(new_destination, file)
                    if file.endswith('.txt'):  #chage it if the annotation is not in txt format
                        with open(file_path, 'r') as f:
                            lines = f.readlines()
            
                        with open(file_path, 'w') as f:
                            for line in lines:
                                line_data = line.split()
                                if line_data:
                                    key = line_data[0]
                                    if key in mapping:
                                        new_key = mapping[key]
                                        line_data[0] = new_key
                                        updated_line = " ".join(line_data) + "\n"
                                        f.write(updated_line)
                                    else:
                                        f.write(line)
                                else:
                                    f.write(line)
        successful_conversion = True
        print(f"Check json on {subfolder} completed")
        
    if successful_conversion:
        print("Successfully converted")
    else:
        print("No folders were successfully converted.")



# Calling  te function to read JSON files in subfolders
#enter the directory for foreign data folder (where you wanna make copies of text files)
foreign_folder = 'insert the foreign directory'  #fill the code here

process_data_from_config(foreign_folder, imported_data)
