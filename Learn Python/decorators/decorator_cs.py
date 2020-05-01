from functools import wraps
import time

# inner function have acces to local variables.

# def outer_function():
# 	msg = 'Hi'
# 	def inner_function():
# 		print(msg)
# 	return inner_function

# -----------------------------------

# def outer_function(msg):
# 	def inner_function():
# 		print(msg)
# 	return inner_function

# hi_func  = outer_function("Hi")
# bye_func = outer_function("Bye")

# hi_func()
# bye_func()

# ----------------
#    Decorator
# ----------------
# A decorator is just a function that takes other function as an argument,
# adds some kind of functionality and then returns another function.
# All of this without altering the source code of original function that you passed in.

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print(f'wrapper executed this before {original_function.__name__}')
		original_function(*args, **kwargs)
		print(f'wrapper executed this after {original_function.__name__}')
	return wrapper_function


@decorator_function
def display():
	print("display function ran")

display()
#	OR

# decorated_display = decorator_function(display)
# decorated_display()

# is same as

# display = decorator_function(display)
# display()
print('-----------------------------------------')

@decorator_function
def display_info(name, age):
	print(f'display_info ran with arguments {name}, {age}')

display_info(name='hasan', age=25)

print('-----------------------------------------')

# ---------------------------
#    Classes as Decorators
# ---------------------------

class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print(f'call method executed this before {self.original_function.__name__}')
		return self.original_function(*args, **kwargs)
		

@decorator_class
def display_info(name, age):
	print(f'display_info ran with arguments {name}, {age}')

display_info(name='hasan', age=25)
print('-----------------------------------------')

# ---------------------------
#    Practical Examples
# ---------------------------

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs)
        )
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# @my_logger
# def display_info(name, age):
# 	print(f'display_info ran with arguments {name}, {age}')

# display_info('adil', age=16)

# @my_timer
# def display_info(name, age):
# 	time.sleep(1)
# 	print(f'display_info ran with arguments {name}, {age}')

# display_info(name='hasan', age=22)


# ----------------------------------------------
#    Multiple Decorators on a single function
# ----------------------------------------------
print("-----------------------------------------")


@my_logger
@my_timer
def display_info(name, age):
	time.sleep(1)
	print(f'display_info ran with arguments {name}, {age}')

display_info(name='hasan', age=22)

# is same as
display_info = my_logger(my_timer(display_info))
print(display_info.__name__)