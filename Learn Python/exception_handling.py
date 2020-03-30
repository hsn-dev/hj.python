#------------------------------#
#     EXCEPTION HANDLING       #
#------------------------------#
#-------------------------------------------------------------------------------------------------------#
#	A single try statement can have multiple except statements.											#	
#   This is useful when the try block contains statements that may throw different types of exceptions. #
#																										#
#	You can also provide a generic except clause, which handles any exception.							#
#																										#
#	After the except clause(s), you can include an else-clause.											#
#   The code in the else-block executes if the code in the try: block does not raise an exception.		#
#																										#
#	The else-block is a good place for code that does not need the try: block's protection.				#
#-------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
#	raise allows you to throw an exception at any time.                                                 	#
#	assert enables you to verify if a certain condition is met and throw an exception if it isn’t.			#
#	In the try clause, all statements are executed until an exception is encountered.						#
#	except is used to catch and handle the exception(s) that are encountered in the try clause.				#
#	else lets you code sections that should run only when no exceptions are encountered in the try clause.	#
#	finally code will always run, with or without any previously encountered exceptions.					#
#-----------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------#
#   Generic Excepion must be placed below the most-specific exceptions  #
#   Otherwise, (1) Generic will be executed.							#
#			   (2) Child will be executed.								#
#-----------------------------------------------------------------------#

#------------------------------------------
class Networkerror(Exception):
   	# def __init__(self, arg):
   	# 	self.args = arg
   	pass

try:
	hostname = 'devnet'
	if hostname == 'devnet':
		raise Networkerror
except Networkerror as e:
	print("Bad Hostname")
#------------------------------------------

try:
    f = open('sample-files/test.txt')

    # Raise Exception Manually

    # if f.name == 'sample-files/test.txt':
    # 	raise Exception
    
    # var = bad_var

except FileNotFoundError:
    print('Sorry. this file does not exist.')
except Exception as e :
	print(f'Something went wrong\n{e}')
else:
	print(f.read())
	f.close()
finally:
	print('Executing Finally')
	