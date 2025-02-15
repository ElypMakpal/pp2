#Implement a generator that returns all numbers from (n) down to 0.
def num(n):
    for i in range(n,0,-1):
        print(i)
n=int(input())
num(n)
