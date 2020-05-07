'''
	var   --> public
	_var  --> protected (can be set&get from outside)
	__var --> private	(can't be set&get from outside)
			  cannot override bcoz of name mangling e.g
			  _Car__model (var-name is altered)
			  _Car__year (var-name is altered)

	same applies for methods...	

'''
class Car:

	def __init__(self, model, year, price, speed):

		self.__model = model
		self.__year  = year
		self.price   = price
		self._speed  = speed

	def get_model(self):
		return self.__model

	def get_year(self):
		return self.__year


class Ferrari(Car):
	def __init__(self, model, year, price, speed):
		super().__init__(model, year, price, speed)

f = Ferrari('xara', '2019', '20500', '300')

print(f.price)
print(f._speed)

print(f.get_model())
print(f.get_year())

print(help(f))

print(dir(f))