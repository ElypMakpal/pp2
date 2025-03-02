# Write a Python program to count the number of lines in a text file.

import os
import string
with open("extext.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()