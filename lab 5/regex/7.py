import re 

with open("1-7exercises.txt") as f:
    data = f.read()

matches=re.sub(r"_",'',data)
print(matches)    