# Write a Python program to calculate the area of regular polygon.
# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625
import math
def regular(sides,l):
    area=((l**2)*sides)/(4*(math.tan(math.pi/sides)))
    print(int(area))
regular(4,25)