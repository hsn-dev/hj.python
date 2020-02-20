# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# generators needs to be iterated for outputs.
# for i in my_gen:
#     print(i)

# Generator Expressions
my_gen = (n*n for n in nums)

# generators needs to be iterated for outputs.
# for i in my_gen:
# 	print(i)

#Generators:
# def cubes(n):
    
#     output = []

#     for x in range(n):
#         output.append(x**3) # every value is stored in memory

#     return output

def cubes(n):
    for x in range(n):
        yield x**3 # just yielding a output and showing on screen, not storing in memory.

# Output
# for x in cubes(100):
#     print(x)

# To get actual list of values
# list(cubes(10))

newFunc = cubes(10)

str  = "Hello" # iterable object
newStr = iter(str) # converted to generator
next(newStr) # next function can be used to move to next yielded value.