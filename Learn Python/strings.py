'''
	Immutable:
		Immutable means once a thing is created or initialized, it cannot be changed or replaced.
    Sequence:
    	Sequence means Indexing and Slicing can be performed on it. 

    message = 'hello world'
    s[1] -> indexing
    s[1:5:2] -> slicing [start: end(upto, not including): step]
    s[::-1]  -> to reverse a string
    s[0] = H -> Error (Strings are immutable)

'''

message = "Hello World"

# String Slicing
print(message[1:5:2])      				# el
print(message[:5])         				# hello
print(message[6:])         				# world
print(message[0:11])       				# hello world
print(message[-1:-12:-1])  				# reverse
print(message[::-1])       				# reverse

# String methods
print(message.upper())     				# HELLO WORLD
print(message.lower())     				# hello world
print(len(message))            			# 11
print(message.count('k'))      			# 3 - no of occurences, else return 0
print(message.find('World'))   			# 6 - find location in string, else return -1

message = message.replace("World", "Universe")
print(message)

# Formatted Strings 
name = "Hassan"
age = 14
phoneNum = "03134743499"
username = "Hassan"
# Method 01
print("my name is {n} and i'm {a} years old. my phone number is {p}".format(n=name, a=age, p=phoneNum))
# Method 02
print(f"my name is {name} and i'm {age} years old. my phone number is {phoneNum}")

print(type(age))
print(id(name))
print(id(username))

# View all attributes and methods available for stored datatype
print(dir(name))
print(help(str.find))