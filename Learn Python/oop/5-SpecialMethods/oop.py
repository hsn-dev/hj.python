# ------------------------------------------------------------------------- #
#   Special Methods in Python:                                              #
#   __repr__ used for logging and debugging by developers                   #
#   __str__  for end-users                                                  #
#   if __str__ is not present then __repr__ will be used as a fallback f()  #
#   print(emp_1)                                                            #
# ------------------------------------------------------------------------- #
#                                                                           #
#                                                                           #
# ------------------------------------------------------------------------- #



class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)

print(len(emp_1))

# BTS: we can customize how addition works for our objects.
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))
