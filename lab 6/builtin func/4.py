#Write a Python program that invoke square root function after specific milliseconds.
import time
import math

def delayed_sqrt(number, num2):
    time.sleep(num2 / 1000)  
    return math.sqrt(number)

num = int(input())  
num2 = int(input())  
result = delayed_sqrt(num, num2)
print(f"Square root of {num} after {num2} milliseconds is {result}")

