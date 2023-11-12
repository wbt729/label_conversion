import json 
import os
#import this file to text_converter_v9.py

class JSONReader:

    def __init__(self, file_name):
        self.file_name = file_name
        
    def read_json(self):
        try:
              with open(self.file_name, 'r') as file:
                   data = json.load(file)
                   return data

        except FileNotFoundError:
             print(f"File not found: {self.file_name}")
         
    def _parse_source_dir(self):
        data = self.read_json()
        if data is not None and "source_directory" in data: 
            source_dir = data["source_directory"]
            if os.path.exists(source_dir):
                pass
                   
            else:
             print(f"the source directory not exists {source_dir}")
        else: 
            print("directory source not found")

    def _parse_target_dir(self):
        data = self.read_json()
        if data is not None and "target_directory" in data: 
            target_dir = data["target_directory"]
            if os.path.exists(target_dir):
                pass

            else:
             print(f"the target directory not exists {target_dir}")
        else: 
            print("target directory not found")

    def _parse_source_labels(self):
        data = self.read_json()
        if data is not None and "source_labels" in data: 
            source_labels = data.get("source_labels", {})
           
                                            #######missing labels
            missing_value = [key for key, value in source_labels.items() if not value ]
            if not missing_value:
                pass
                
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
