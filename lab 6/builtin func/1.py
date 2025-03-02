# Write a Python program with builtin function to multiply all the numbers in a list

import math

def multiply_list (a):
    return math.prod(a)

# Example usage
a=[]
n=int(input())
for i in range (n):
    a.append(input())
a = list(map(int, a))  

print("multiply all the numbers in a list: " , multiply_list(a))  # Output: 120
