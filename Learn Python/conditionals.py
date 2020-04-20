# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

language = 'java'
if language == 'python':
	print('Language is python')
elif language == 'java':
	print('Language is java')
else:
	print('No Match')

user = 'admin'
logged_in = True

# and
# or
# not
if user == 'admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Credentials')

if not logged_in:
	print('please login')
else:
	print(f'Welcome {user}')

# object identity
a = [1,2,3]
b = [1,2,3]
# a = b
print(f'address of a: {id(a)}')
print(f'address of b: {id(b)}')
print(f'a == b ({a == b})')
print(f'a is b ({a is b})') # id(a) == id(b)

condition = ''
if condition:
	print('Evaluated to True')
else:
	print('Evaluated to False')

# ---------------------------- #
#     SWITCH STATEMENT         #
# ---------------------------- #

def switch(case):
	
	return {

		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six'

	}.get(case, "No Match Found")

x = switch(6)
print(x)