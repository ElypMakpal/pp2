import re 


with open("10-ex.txt") as f:
    data = f.read()

matches=re.sub(r"[A-Z]",'_',data)
print(matches)