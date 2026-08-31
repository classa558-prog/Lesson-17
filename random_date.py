import time
import random
print("Welcome to random date generator!")
start_date = input("Enter your starting date in the format, mm/dd/yyyy.")
ending_date = input("Enter your ending date in the format, mm/dd/yyyy.")
date_format = '%m/%d/%Y'
start_time = time.mktime(time.strptime(start_date, date_format))
end_time = time.mktime(time.strptime(ending_date, date_format))
r = random.random()
random_time = ((end_time - start_time)*r)+start_time
random_date = time.strftime(date_format, time.localtime(random_time))
print(f"A random date between {start_date} and {ending_date} is: {random_date}")
