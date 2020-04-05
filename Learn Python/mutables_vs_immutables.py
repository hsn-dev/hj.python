'''
A mutable object can be changed after it is created, and an immutable object can't.

The key thing to note is that the bindings are unchangeable, not the objects they are bound to.
Let us consider a tuple t = (‘holberton’, [1, 2, 3])

This is a subtle point, but nonetheless important: the “value” of an immutable object can’t change,
 but it’s constituent objects can.
'''

# IMMUTABLES
a = "hassan"
print(f'Addres of a: {id(a)}')

a = "farooq"
print(f'Addres of a: {id(a)}')

# MUTABLES
l = [1,2,3,4,5]
print(l)
print(f'Addres of list: {id(l)}')

l[0] = 6
print(l)
print(f'Addres of list: {id(l)}')