import re 

with open("1-7exercises.txt") as f:
    data = f.read()

matches = re.findall(r"[A-Z][a-z]+", data)
print(matches)