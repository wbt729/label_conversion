# label_conversion--

This converter helps to change the labels of already annotated images, 
so that you can combine different data sets. 

After downloading the label_conversion, neccessary changes to make.

## Step 1: Changes to make in text_converter.py file:

#### Step 1.1: insert the directory of imported_data, 
I commented: fill the code here , line 8.<br>

#### Step 1.2 insert the directory of foreign_folder: 
I commented:  fill the code here, line 94. <br>

## Step 2: Edit the directories of Configuration.json

#### Step 2.1: 
open each Configuration.json file in sub folders of foreign data one by one <br>

#### Step 2.2: 
change the source directory with the actual path of the data folder, where all the actal txt files exist <br>
e.g '... /Desktop/label_conversion/foreign_data/Board_wood_data/data' <br>

#### Step 2.3: 
change the target directory with the actual path of imported data, where all the converted text files going to be created (imported_data) <br>
e.g  '... /Desktop/label_conversion/imported_data'<br>
      
#### Step 2.4: 
Change the mapping according to your source labels and target labels <br>











