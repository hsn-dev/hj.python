# Working with file objects



# default: opens a file for reading
# options: 'r' -> reading
# 		   'w' -> writing
#		   'a' -> appending
#		  'r+' -> read and write

# f = open('sample-files/test.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()



## Context Managers automatically close a file.

# with open('sample-files/test.txt', 'r') as f:
# 	pass
# print(f.closed)
# print(f.read())



## read() -> whole content at once

# with open('sample-files/test.txt', 'r') as f:
# 	f_contents = f.read()
# 	print(f_contents)



## readlines() -> returns a list of whole content

# with open('sample-files/test.txt', 'r') as f:
# 	f_contents = f.readlines()
# 	print(f_contents)



## readline() -> reads one line at a time

# with open('sample-files/test.txt', 'r') as f:
# 	f_contents = f.readline()
# 	print(f_contents, end='')

# 	f_contents = f.readline()
# 	print(f_contents, end='')



## Using loop to read a single line

# with open('sample-files/test.txt', 'r') as f:
# 	for line in f:
# 		print(line, end='')



## read(n) -> reads first 'n' characters
#  returns empty string if reached EOF

# with open('sample-files/test.txt', 'r') as f:
# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# 	f_contents = f.read(100)
# 	print(f_contents, end='')



## Using While loop to read characters

# with open('sample-files/test.txt', 'r') as f:
# 	size_to_read = 10
# 	f_contents = f.read(size_to_read)
# 	while len(f_contents) > 0:
# 		print(f_contents, end='*')
# 		f_contents = f.read(size_to_read)



## tell() -> current position of the cursor in file
## seek() -> goes to the specific position in file

# with open('sample-files/test.txt', 'r') as f:
# 	size_to_read = 10

# 	f_contents = f.read(size_to_read)
# 	print(f_contents)

# 	f.seek(0)

# 	f_contents = f.read(size_to_read)
# 	print(f_contents)

# 	print("Current position of cursor: ",f.tell())


## Write to a file
#  ---------------------------------------------------------
#  if try to write a file in read mode, then
#  io.UnsupportedOperation: not writable
#  ---------------------------------------------------------
#  FILE MODE: w
#  ---------------------------------------------------------
#  if file already exists then it will overrite it,
#  else it will create a new file with that name.
#  ---------------------------------------------------------
#  FILE MODE: a
#  ---------------------------------------------------------
#  if file already exists then it will append to it,
#  else it will create a new file with that name.
#  ---------------------------------------------------------
#  FILE MODE: r
#  ---------------------------------------------------------
#  File needs to be present for read operation,
#  if not exist then error.
#  ---------------------------------------------------------
#  FILE MODE: Binary Mode (b)
#  ---------------------------------------------------------
#  it can be used with r/w to work with binary files
#  e.g to copy image files

with open('sample-files/test2.txt', 'w') as f:
	f.write('test')
	f.seek(3)
	f.write('la')
	f.seek(0)
	f.write('Cer')

with open('sample-files/test2.txt', 'a') as f:
	f.write('test')


with open('sample-files/test.txt', 'r') as rf:
	with open('sample-files/test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

# with open('sample-files/codesnap.png', 'rb') as rf:
# 	with open('sample-files/codesnap_copy.png', 'wb') as wf:
# 		for line in rf:
# 			wf.write(line)

with open('sample-files/codesnap.png', 'rb') as rf:
	with open('sample-files/codesnap_copy.png', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)




