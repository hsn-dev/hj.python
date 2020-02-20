'''
	LEGB: Local, Enclosing, Global, Built-in
	scope check: left to right

'''

x = 'global x'
# y = 'global y'

def test():
	y = 'local y'
	print(y)
	print(x)

test()
print("--------------")

def test1():
	x = 'local x'
	print(x)

test1()
print("--------------")

def test2():
	global x
	x = 'local x'
	print(x)

test2()
print(x)
print("--------------")

def test3():
	global y
	y = 'local y'
	print(y)

test3()
print(y)
print("--------------")

# Local:
def test4(z):
	print(z)

test4("local z")

# Built-in
import builtins
# reserved words
# print(dir(builtins))
# def min():
# 	pass 
print(min([4,5,6,2]))

# Enclosing
x = 'global me'
def outer():
	x = 'outer x'
	def inner():
		# nonlocal x
		x = 'inner x'
		print(x)
	inner()
	print(x)
outer()
print(x)