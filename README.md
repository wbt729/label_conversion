# label_conversion

This converter helps to change the labels of already annotated images, 
so that you can combine different data sets. 

After downloading the label_conversion, neccessary changes to make.

Step 1: Change the to make in text_converter.py file:
1.1 insert the directory of imported_data, line 8. I commented: fill the code here..
1.2 insert the directory of foreign_folder, line 94. I commented:  fill the code here..

Step 2: Edit the directories of Configuration.json
2.1: open each Configuration.json file in sub folders of foreign data one by one 
2.2: change the source directory with the actual path of the data folder
      where all the actal txt files are
      e.g '... /Desktop/label_conversion/foreign_data/Board_wood_data/data'
2.3: change the target directory with the actual path of imported data
      where all the converted text files gonna be created (imported_data)
      e.g  '... /Desktop/label_conversion/imported_data'
2.4: Change the mapping according to your source labels and target labels











