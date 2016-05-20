#to pass command line arguments, need to import separate argv from sys
from sys import argv  
import os.path # for the path validation and include exists

#Below line is used to store the arguments passed in the cmd line
script, folder_name, file_name = argv

txt = """this is the content to be written
using python"""

base_path = 'C:\\Python27\\practice\\'
path_folder = base_path+folder_name
path_file = base_path+file_name

#to check if the folder exists at the specified path
if os.path.exists(path_folder):
    print "Folder exists"
else:
    os.mkdir(folder_name)

#to check if the file exists at the specified path
if os.path.isfile(path_file):
    print "File exists"
else:
   f=open(file_name, 'wt')
   f.write(txt)
   f.close()




