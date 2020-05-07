# Modules vs Packages
# Modules are .py files which we include in other .py file.
# Packages are collection of modules i.e __init__.py should be included in a folder 
# so python know that these .py files should be treated as a package.


from MainPackage import m1
from MainPackage.SubPackage import s1
# from MainPackage.m1 import main_func

m1.main_func()

s1.sub_func()