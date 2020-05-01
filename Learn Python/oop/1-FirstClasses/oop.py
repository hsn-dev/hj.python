# ------------------------------------------------------------------------- #
#   if we remove self from any method then we get error                     #
#   in our case, fullname(): => TypeError: takes 0 args but 1 was given.    # 
#   this means our calling object is passed as an argument to method.       #
# ------------------------------------------------------------------------- #
#   emp_1.fullname()          | is equivalent to |                          #
#	Employee.fullname(emp_1)                                                #
# ------------------------------------------------------------------------- #

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'

emp_1 = Employee('hasan', 'farooq', 55000)
emp_2 = Employee('adil', 'farooq', 65000)

emp_1.fullname()
Employee.fullname(emp_1)