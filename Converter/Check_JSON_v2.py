import json 
import os


#i wanna import this file to text converter

class JSONReader:

    def __init__(self, file_name):
        self.file_name = file_name
        

    def read_json(self):
        try:
              with open(self.file_name, 'r') as file:
                   data = json.load(file)
                 # to check only if the file is openning bc of wrong directory
                 # its for us, bc if the terminal directory is not in the.. 
                 # same folder its not gonna inform to change the directory 
                 # print(json.dumps(data))
                #    print("file found.. (this message is from the read_json :p)")
                   return data

        except FileNotFoundError:
             print(f"File not found: {self.file_name}")



            
    def _parse_source_dir(self):
        data = self.read_json()
        if data is not None and "source_directory" in data: 
            source_dir = data["source_directory"]
            # print(f"source directroy: {source_dir}")          #i removed the print because i dont want it with the merged code
            # now checking if the path exists or not 
            if os.path.exists(source_dir):
                pass
                    # print(f"the source directory exists {source_dir}")    #i removed the print because i dont want it with the merged code
            else:
             print(f"the source directory not exists {source_dir}")
        else: 
            print("directory source not found")



    def _parse_target_dir(self):
        data = self.read_json()
        if data is not None and "target_directory" in data: 
            target_dir = data["target_directory"]
            # print(f"target directroy: {target_dir}")          #i removed the print because i dont want it with the merged code
            ## now checking if the path exists or not 
            if os.path.exists(target_dir):
                pass
                    #print(f"the target directory exists {target_dir}")     #i removed the print because i dont want it with the merged code
            else:
             print(f"the target directory not exists {target_dir}")
        else: 
            print("target directory not found")


    def _parse_source_labels(self):
        data = self.read_json()
        if data is not None and "source_labels" in data: 
            source_labels = data.get("source_labels", {})
            #seen_labels = set()
            #print("source labels found")                       #i removed the print because i dont want it with the merged code
            # print(f"{source_labels}")
                                            #######missing labels
            missing_value = [key for key, value in source_labels.items() if not value ]
            if not missing_value:
                pass
                #print("all values in 'source_labels' are defined.")            #i removed the print because i dont want it with the merged code
            else:
                 print("Source Labels is missing.")  
                                            ######3 unique labels
            seen_labels_source_labels = set()
            non_unique_labels_source_labels =[]
            for key, value in source_labels.items():
                if value in seen_labels_source_labels:
                    non_unique_labels_source_labels.append(key)
                    non_unique_labels_source_labels.append(value)
                seen_labels_source_labels.add(value)
            
            if not non_unique_labels_source_labels:
                pass
                #print("All labels in 'Source_labels' are Unique")          #i removed the print because i dont want it with the merged code

            else:
                print("Non-unique Labels in Source directory: ",non_unique_labels_source_labels)

        else: 
            print("source labels not found")


    def _parse_target_labels(self):
        data = self.read_json()
        if data is not None and "target_labels" in data: 
            target_labels = data.get("target_labels", {})
            
            # Create a set to keep track of seen keys and labels
            seen_target_keys = set()
            seen_target_labels = set()

            # Create lists to store missing or duplicate keys and labels
            missing_or_duplicate_target_keys = []
            missing_or_duplicate_target_labels = []

            # Check if all keys and labels in "target_labels" are correct and track missing or duplicate keys and labels
            for key, value in target_labels.items():
                if not key.isdigit() or key in seen_target_keys:
                    missing_or_duplicate_target_keys.append(f'Key "{key}" is not a valid key {key}')
                seen_target_keys.add(key)

                if value == "" or value in seen_target_labels:
                    missing_or_duplicate_target_labels.append(f'"" label index {key}')
                elif value in seen_target_labels:
                    missing_or_duplicate_target_labels.append(f'Label "{value}" is duplicated {key}')
                seen_target_labels.add(value)

            if not missing_or_duplicate_target_keys and not missing_or_duplicate_target_labels:
                pass
                #print("All keys and labels in 'target_labels' are correct.")       #i removed the print because i dont want it with the merged code
            else:
                if missing_or_duplicate_target_keys:
                    print("Key errors:")
                    for error in missing_or_duplicate_target_keys:
                        print(error)
                if missing_or_duplicate_target_labels:
                    print("Label errors:")
                    for error in missing_or_duplicate_target_labels:
                        print(error)
        else: 
            print("target labels not found")


    def _parse_mapping(self):
        data = self.read_json()
        if data is not None and "mapping" in data:
            mapping = data.get("mapping", {})
            
            # Create a set to keep track of seen source keys and target keys
            seen_key1_mapping = set()
            seen_key2_mapping = set()

            # Create lists to store missing or duplicate keys
            missing_or_duplicate_key1_mapping = []
            missing_or_duplicate_key2_mapping = []

            # Check if all source and target keys in "mapping" are correct and track missing or duplicate keys
            for source_key, target_key in mapping.items():
                if not source_key.isdigit() or source_key in seen_key1_mapping:
                    missing_or_duplicate_key1_mapping.append(f'Source Key "{source_key}" is not a valid key at index {source_key}')
                seen_key1_mapping.add(source_key)

                if not target_key.isdigit() or target_key in seen_key2_mapping:
                    missing_or_duplicate_key2_mapping.append(f'Target Key "{target_key}" is not a valid key at index {source_key}')
                seen_key2_mapping.add(target_key)

            if not missing_or_duplicate_key1_mapping and not missing_or_duplicate_key2_mapping:
                pass
                #print("All labels and keys in 'mapping' are correct.")         #i removed the print because i dont want it with the merged code
            else:
                if missing_or_duplicate_key1_mapping:
                    print("Source Key errors:")
                    for error in missing_or_duplicate_key1_mapping:
                        print(error)
                if missing_or_duplicate_key2_mapping:
                    print("Target Key errors:")
                    for error in missing_or_duplicate_key2_mapping:
                        print(error)
        else: 
            print("mapping not found")




   
# # running all the functions
# json_reader = JSONReader('Configuration.json')
# json_reader.read_json()
# json_reader._parse_source_dir()
# json_reader._parse_target_dir()
# json_reader._parse_source_labels()
# json_reader._parse_target_labels()
# json_reader._parse_mapping()