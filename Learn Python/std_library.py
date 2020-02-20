import random
import math
import datetime
import calendar
import os

fruits = ['apple', 'banana', 'mango', 'strawberry', 'blueberry']

random_fruit = random.choice(fruits)
print(random_fruit)

rads = math.radians(90)
print(f'90 degree in radians: {rads}')
print(f'Sine of 90 deg: {math.sin(rads)}')

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# cwd -> current working directory
print(os.getcwd())

# path of os module file
print(os.__file__)



