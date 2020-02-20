def hello_func():
	print('hello world')

print(hello_func())

def wish(greeting, name='Hasan'):
	return f'Happy {greeting} to {name}'

print(wish('birthday', 'hasan').upper())
print(wish('Eid'))
print(wish('birthday', name="Hamza"))

# *args    => tuple
# **kwargs => dict 
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['maths', 'eng']
info = {'name': 'hasan', 'age': 14}
# student_info('maths', 'eng', name='hasan', age=14)	
student_info(*courses, **info)

# kwargs - keyword arguments
# passing arbitrary number of dictionary to a function
def zen(**kwargs):
	print(f"i like {kwargs['fruit']}, {kwargs['vegie']} and {kwargs['cow']}")

zen(fruit='apple', vegie='tomato', cow='milk')

# args - tuple arguments
# passing arbitrary number of tuple in a function
def tup(*args):
	print(args)
	for item in args:
		print(item * 5, end=' ')

tup(1,2,3,4,5,6,7,8,9,10)

# Examples
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print()
print(f'Days in month: {days_in_month(2020, 2)}')