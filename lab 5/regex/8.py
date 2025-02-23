import re 


with open("row-8-10-ex.txt") as f:
    data = f.read()
    
print(re.findall(r"[A-Z][^A-Z]*", data))