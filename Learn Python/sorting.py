from operator import attrgetter
# Sorting List

li = [9,1,6,2,6,4,7,5,3,0]

print(f'Original List: {li}')

# @param bool reverse
# returns a list
sorted_li = sorted(li)
print(f'Sorted List using sorted():    {sorted_li}')

# @param bool reverse
# return None
li.sort() 
print(f'Sorted List using li.sort():   {li}')

# Sorting Tuple
tup = (9,1,6,2,6,4)
s_tup = sorted(tup)
print(f'Sorted Tuple:                  {s_tup}')

# Sorting Dictionary
student = {
	'name': 'Hassan',
	'age': 21,
	'courses': ['Maths', 'CompSci']
}
sorted_dict = sorted(student)
print(f'Sorted Dict:                   {sorted_dict}')

# Sorting example
li = [-6,-5,-4,1,2,3]
s_list = sorted(li, key=abs)
print(f'Sorted List as key=abs:        {s_list}')

# Sorting Objects
class Employee():
	def __init__(self, name, age, salary):
		self.name   = name
		self.age    = age
		self.salary = salary
	def __repr__(self):
		return f"Name: {self.name}, Age: {self.age} & Salary: ${self.salary}"

e1 = Employee("Hassan", "21", "47000")
e2 = Employee("Farooq", "11", "37000")
e3 = Employee("Adil", "16", "50000")

employees = [e1, e2, e3]

def e_sort(emp):
	return emp.name

# s_emp = sorted(employees, key=e_sort)
# s_emp = sorted(employees, key = lambda e: e.name)
s_emp = sorted(employees, key=attrgetter('age'), reverse=True)

for index, emp in enumerate(s_emp):
	print(index, emp)