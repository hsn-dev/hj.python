'''
	Duck Typing and Easier To Ask Forgiveness than Permission (EAFP)

	Duck Typing is a concept in which we don't care about what type of object are we working with 
	we only care if our object can do what we ask it to do it.

'''

class Duck:

	def quack(self):
		print('Quack, Quack')

	def fly(self):
		print('Flap, Flap')

class Person:

	def quack(self):
		print("I'm quacking like a duck!")

	def fly(self):
		print("I'm flapping my arms!")


def quack_and_fly(thing):
    pass

    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Non-Pythonic)
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    # EAFP (Pythonic)
    #     try:
    #         thing.quack()
    #         thing.fly()
    #         thing.bark()
    #     except AttributeError as e:
    #         print(e)