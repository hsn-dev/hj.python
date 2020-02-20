

# MUTABLES
a = "hassan"
print(f'Addres of a: {id(a)}')

a = "farooq"
print(f'Addres of a: {id(a)}')

# IMMUTABLES
l = [1,2,3,4,5]
print(l)
print(f'Addres of list: {id(l)}')

l[0] = 6
print(l)
print(f'Addres of list: {id(l)}')