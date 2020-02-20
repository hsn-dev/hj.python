import sys
# if module is not present in the same directory of running script.
# sys.path.append("reference to module directory")
# or
# we need to set env variable in system. var name: PYTHONPATH

# import my_module
import my_module as md
# from my_module import find_index (no need to prepend with module name)
# from my_module import find_index, test
# from my_module import *
# from my_module import find_index as fi, test as t

courses = ['History', 'Math', 'Physics', 'CompSci']

x = md.find_index(courses, 'Math')
print(f'index location: {x}')

''' ~ how to find out from where system gets module path?
	> import sys
	> sys.path
'''
print(sys.path)