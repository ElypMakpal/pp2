#Write a Python program to calculate two date difference in seconds.
import datetime

date1 = datetime.datetime(2024, 2, 10, 12, 0, 0)
date2 = datetime.datetime(2024, 2, 13, 15, 30, 0)

difference_in_seconds = abs((date2 - date1).total_seconds())
print(date1)
print(date2)
print("Difference in Seconds:", difference_in_seconds)
