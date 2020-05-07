

class Employee:

	def __init__(self, fname, lname):
		# instance variables
		self.fname    = fname
		self.lname    = lname

	def get_fullname(self):
		return f'{self.fname} {self.lname}'

	def set_fullname(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def get_email(self):
		return f'{self.fname}.{self.lname}@gmail.com'

	@property
	def fullname(self):
		return self.fullname

	@fullname.setter
	def fullname(self, name):
		fname, lname = name.split(" ")
		self.fname = fname
		self.lname = lname

	@property
	def email(self):
		return f'{self.fname}.{self.lname}@gmail.com'
	


emp1 = Employee('hasan', 'farooq')