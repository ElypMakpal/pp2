# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

import os
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path,os.W_OK):
            try:
                os.remove(file_path)
                print(f"file {file_path} delete") 
            except Exception as e:
                print("Error")
                
                
        else:
            print("You do not have write access")
    else:
        print(f"File '{file_path}' does not exist.")
            
        


path_delete=str(input("path_delere_file:"))

delete_file(path_delete)

#   path_delere_file:Z.txt
#   file Z.txt delete