'''
	Data Structure:
		It is a way to store and organize data in a efficent manner so that
		we can perform operations on data like searching and sorting.

	Sequence: List, Tuple
	Mapping:  Dict
	Collection: Set

	Mutables: List, Dict, Sets
	Immutables: Tuples

	Set:      unordered collection of unique elements.
	Tuple:    immutable sequence.
	List:     mutable sequence.
	Mappings: unordered and mutable  
    

'''
# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

#-----------------------#
#       L I S T         #
#-----------------------#
courses = ['english', 'urdu', 'maths', 'comp']
courses2 = ['chemistry', 'biology']
print(len(courses))
print(courses[0])
courses.append("islamiyat")
courses.insert(0, "physics")
courses.extend(courses2)
courses.remove('physics')
print(courses)
courses.reverse()
print(courses)
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
sorted_list = sorted(courses)
print(sorted_list)

nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index("maths"))
print("Maths" in courses)

for course in courses:
	print(course)

for index, course in enumerate(courses,  start=1):
	print(index, course)

# To convert list into string:
course_str = ' - '.join(courses)
print(course_str)

# To convert String into List:
new_list = course_str.split(' - ')
print(new_list)

# To remove last element: LIFO
new_list.pop()
# To remove by index: 
new_list.pop(3)

# Problem
list_1 = ['Apple', 'Orange', 'Banana', 'Strawberry']
list_2 = list_1
# Solution
# list_2 = list(list_1)

list_1[0] = 'Mango'

print(list_1)
print(list_2)

#-----------------------#
#     T U P L E S       #
#-----------------------#
t = ('bmw', 'honda', 'gtr', 'honda')
# not allowed
# t[0] = 'ford' 
print(t.index('honda'))  # 1
print(t.count('honda'))  # 2
print(sorted(t))


#-----------------------#
#        S E T          #
#-----------------------#
s = set(t)
print(s)
# Sets are optimized for membership test.
print('bmw' in s)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 3, 2, 7, 9, 8}

print(f'Intersection: {s1.intersection(s2)}')
print(f'Union: {s1.union(s2)}')
print(f'Difference: {s1.difference(s2)}')


#-------------------------#
#   D I C T I O N A R Y   #
#-------------------------#
student = {
	'name': 'Hassan',
	'age': 21,
	'courses': ['Maths', 'CompSci']
}


print(student)
# If key not exist, gives key-error
# print(student['phone'])
x = student.get('phonenumber', 'not found')
if 'not found' in x:
	print("Phone Number Not Found")

# enter new value or update value
student['phonenumber'] = '03004336368' 
print(student)
# update multiple values at one time
student.update({'name': 'Hamza', 'age': 22, 'address': 'Lahore'})
print(student)
# delete a value
del student['age']
# or
address = student.pop('address')
# Number of keys in dict
print(len(student))
# Print Keys
print(student.keys())
# Print Values
print(student.values())
# Print key-value 
print(student.items())
# Loop through dict
for item in student.items():
	print(type(item)) #tuples

for key, value in student.items():
	print(f'Key: {key}, Value: {value}')

