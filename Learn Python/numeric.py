'''
	Arithmetic Operators:
		Addition:          3 + 2
		Subtraction: 	   3 - 2
		Multiplication:    3 * 2
		Division:          3 / 2
		Floor Division:    3 // 2
		Exponent:		   3 ** 2
		Modulus:           3 % 2
'''

num = 3 / 2
print(f'Value: {num}')
print(f'Type: {type(num)}')

num = 3 // 2  # result: 1
num = num + 1 # num++ not supported
num += 1
print(f'Result: {num}')

# Built-in Methods:

# Absolute Function:
print(abs(-47))
# Round off first digit after the decimal
print(round(3.75, 1))

'''
	Comparison Operators:
		Equal:              3 == 2
		Not Equal:		    3 != 2
		Greater than:       3 > 2
		Less than:			3 < 2 
		Greater or Equal:   3 >= 2
		Less or Equal:      3 <= 2
'''
print(3 >= 2)

# Type Casting:
num1 = '100'
num2 = '200'
result = int(num1) + int(num2)
print(result)
