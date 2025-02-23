import re 

with open("1-7exercises.txt") as f:
    data = f.read()


matches = re.findall("a.*bb+|abbb+", data)
print(matches)
