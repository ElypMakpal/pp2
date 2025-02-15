#Define a function with a generator which can iterate the numbers, 
# which are divisible by 3 and 4, between a given range 0 and n.
n=int(input())
for i in range (0,n+1):
    if (i%3==0)&(i%4==0):
        if i==0:
            continue
        print(i)
    else:
        continue