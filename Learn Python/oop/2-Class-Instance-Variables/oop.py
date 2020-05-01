# ------------------------------------------------------------------------- #
#   if we remove self from any method then we get error                     #
#   in our case, fullname(): => TypeError: takes 0 args but 1 was given.    # 
#   this means our calling object is passed as an argument to method.       #
# ------------------------------------------------------------------------- #
#   emp_1.fullname()          | is equivalent to |                          #
#	Employee.fullname(emp_1)                                                #
# ------------------------------------------------------------------------- #

class Employee:

	num_of_employees = 0
	raise_amount = 0.4

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.num_of_employees += 1
	
	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('hasan', 'farooq', 65000)
emp_2 = Employee('adil', 'farooq', 65000)

emp_1.raise_amount = 0.5

print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

emp_1.apply_raise()
emp_2.apply_raise()

print(emp_1.pay)
print(emp_2.pay)

print(f'Number of Employees: {Employee.num_of_employees}')