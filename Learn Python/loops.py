'''
	break:    terminates the loop
	continue: move to next iteration
'''



nums = [1,2,3,4,5]

# break
for num in nums:
	if num == 3:
		print('found', end=' ')
		break
	print(num, end=' ')

# continue
print()
for num in nums:
	if num == 3:
		print('found', end=' ')
		continue
	print(num, end=' ')

# nested loops
print()
for num in nums:
	for letter in 'abc':
		print(num, letter, end='    ')
	print()

print('---------------')
# while loop
x = 0
while x < 10:
	if x == 5:
		break
	print(x)
	x += 1

print('---------------')
# do while loop
i = 1  
while True:  
    print(i)  
    i += 1
    if(i > 5):  
        break  

#-----------------------#
#    ELSE WITH LOOP     #
#-----------------------#

# ELSE: No-Break
# If No Break statement is hit in a loop, then run Else statement.

print('---------------')
print("ELSE WITH LOOP")

my_list = [1,2,3,4,5]

for i in my_list:
	print(i)
	if i == 3:
		break
else:
	print('Hit the for/else statement!')

# REAL EXAMPLE
def find_index(to_search, key):
	for i, value in enumerate(to_search):
		if value == key:
			break
	else:
		return -1
	return i

my_list = [33, 24, 54, 47, 21]
loc = find_index(my_list, 47)
print(f'Location of Target is: {loc}')