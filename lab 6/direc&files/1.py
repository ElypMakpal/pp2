# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

path= r"C:\pp2\lab 6\direc&files"
all=list(os.listdir(path))
print(all)