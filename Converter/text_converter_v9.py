import os
import shutil
import json
from converter_final import JSONReader  # Importing the JSONReader class


# Specify the path to the GLES directory
gles_folder = '/Users/syedaffaniqbal/Desktop/try_home_office/GLES'  

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
    for subfolder in os.listdir(source_folder):
        subfolder_path = os.path.join(source_folder, subfolder)
        if os.path.isdir(subfolder_path):
            config_data = find_and_load_config_file(subfolder_path)

            if config_data:


                json_reader = JSONReader(os.path.join(subfolder_path, 'Configuration.json'))
                json_reader.read_json()
                json_reader._parse_source_dir()
                json_reader._parse_target_dir()
                json_reader._parse_source_labels()
                json_reader._parse_target_labels()
                json_reader._parse_mapping()

                # json_reader = JSONReader('Configuration.json')
                # json_reader = json_reader.read_json()
                # json_reader._parse_source_dir()
                # json_reader._parse_target_dir()
                # json_reader._parse_source_labels()
                # json_reader._parse_target_labels()
                # json_reader._parse_mapping()       



                # Extract data frm json fiel
                source_dir = os.path.join(subfolder_path, 'data')  # Adjust source directory as needed
                # target_dir = config_data["target_directory"]
                # source_labels = config_data["source_labels"]
                # target_labels = config_data["target_labels"]

                #i can skip these statements but they can be usefull..

                mapping = config_data["mapping"]

                # Create a new directory within the GLES directory with the specified folder name
                # to be sure about the data and dont mix up data
                #shall i also include the date in the folder name??
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
                #got this code from youtube..
                for file in os.listdir(new_destination):
                    file_path = os.path.join(new_destination, file)
                    if file.endswith('.txt'):  # I can chage it if the annotation is not in txt format
                        with open(file_path, 'r') as f:
                            lines = f.readlines()
            # working..
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

        print(f"Check json on {subfolder} completed")
    print("Successfully converted")

#i need an else statement too if the file not found but im thing to merge the Configuration_check_file too!

#idea is to make 2 file and import the Configuration_check_file in this code... (working)

# Calling  te function to read JSON files in subfolders
process_data_from_config('/Users/syedaffaniqbal/Desktop/try_home_office/foreign_data', gles_folder)
