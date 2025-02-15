#Write a Python program to subtract five days from current date.
import datetime
x = datetime.datetime.now()
day=int(x.strftime("%d"))
print(day-5)

