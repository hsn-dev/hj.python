
# ------------------------------ #
#   Function Without Generator   #
# ------------------------------ #

# def square_numbers(nums):
# 	''' 
# 		@param nums: list
# 		@return list: square of numbers
# 	'''
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result

# ---------------------------------------------------------- #
#   Using Generator 									     #
#   >>> Generators don't hold the entire result in memory.   #
#   >>> It yields one result at a time.                      #
#   >>> It waits for us to ask for next result.              #
# ---------------------------------------------------------- #

def square_numbers(nums):
	''' 
		@param nums: list
		@return list: square of numbers
	'''
	result = []
	for i in nums:
		yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

# my_nums = [x*x for x in [1,2,3,4,5]]	  # List Comprehension
# my_nums = (x*x for x in [1,2,3,4,5])    # Generator

print(my_nums)          # it hasn't computed anything yet!
print(next(my_nums))    # 1
print(next(my_nums))    # 4
print(next(my_nums))    # 9 
print(next(my_nums))    # 16
print(next(my_nums))    # 25	

# ------------------------------------- #
#   For Loop takes care of next(),      #
#   as it knows when to stop the loop   #
# ------------------------------------- #

for num in my_nums:
	print(num)

# ------------------------------------- #
#   Convert Generator to List           #
# ------------------------------------- #

list(my_nums)