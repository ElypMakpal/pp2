import re 

with open("1-7exercises.txt") as f:
    data = f.read()

matches = re.findall("[a-z]_+[a-z]+", data)
print(matches)