# ---------------------------- #
#     TOOLS FOR DECORATOR      #
# ---------------------------- #

# Passing a function as parameter to another function

def outer_func(orig_func):
	print("Some Code Here...")
	orig_func()

# Return a function from inside a function

def hello(name="Hasan"):
	print("The hello() func has been executed.")

	def greet():
		print("\tThis is a greet() func inside hello()")
	def welcome():
		print("\tThis is a welcome() func inside hello()")

	print("I'm going to return a function")

	if name == 'Hasan':
		return greet
	else:
		return welcome

# my_new_func = hello()
# print(my_new_func())

# ---------------------------- #
#     D E C O R A T E R        #
# ---------------------------- #

def new_decorator(original_func):

    def wrap_func():

        print("Some text before the function.")
        original_func()
        print("Some text after the function.")

    return wrap_func

def func_need_decor():
    print("I need to be decorated!!!")

# decorated_func = new_decorator(func_need_decor)
# decorated_func()


#works as a switch just comment it out and old function functionality will be lost.
@new_decorator # comment me for on and off
def func_need_decor():
    print("I need to be decorated!!!")

func_need_decor()