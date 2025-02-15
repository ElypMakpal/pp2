#Write a Python program to print yesterday, today, tomorrow.
# from datetime import datetime, timedelta
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday.strftime("%d.%m.%Y (%A)"))
print("Today:", today.strftime("%d.%m.%Y (%A)"))
print("Tomorrow:", tomorrow.strftime("%d.%m.%Y (%A)"))


