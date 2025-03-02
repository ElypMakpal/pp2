#  Write a Python program to test whether a given path exists or not.
#  If the path exist find the filename and directory portion of the given path.


import os
path= r"C:\pp2\lab 6\direc&files"
def checker(path):
    if os.path.exists(path):
        print("Name of file: ", os.path.basename(path))
        print("name of directory: ", os.path.dirname(path))
        return "success"
    
print(checker(path))