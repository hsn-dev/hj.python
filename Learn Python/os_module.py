import os 
from datetime import datetime
# os module allows us to interact with the underlying operating system.

# print(help(os))
# print(dir(os))

# print(os.name)
# print(os.path)

# print(os.getcwd())
# os.chdir('C:\\Users\\Hasan\\Desktop\\hsn@dev9t')
# print(os.getcwd())

# print(os.listdir())

# Create directory at current level of hierarchy
# os.mkdir("mydir")
# Create directory multilevel deep
# os.makedirs('mydir/subdir')

# Remove directory at current level of hierarchy
# os.rmdir("mydir")
# Remove directory multilevel deep
# os.removedirs('mydir/subdir')

# Rename a file
# os.rename(current, new)
# os.rename('hammy.txt', 'hsn.txt')

# Display information of file
# mod_time = os.stat('hsn.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# os.walk() => display directory in tree format
# it returns a tuple (dirpath, directories in that path, files in that path)

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
# 	print('Current Path:', dirpath)
# 	print('Dirnames:', dirnames)
# 	print('Filenames:', filenames)
# 	print()

# Get Environment variables
print(os.environ.get('USERNAME'))

# To join two paths
file_path = os.path.join(os.environ.get('USERNAME'), 'test.txt')
print(file_path)

# Directory Name:
print(f'Dirname: {os.path.dirname(os.getcwd())}')
# BaseName:
print(f'Basename: {os.path.basename(os.getcwd())}')
# Split both
print(f'Split Both: {os.path.split(os.getcwd())}')
# Path exists
print(f'Path Exists: {os.path.exists(file_path)}')
# Is Directory?
print(f'Is Dir: {os.path.isdir(os.getcwd())}')
# Is File?
print(f'Is File: {os.path.isfile(os.getcwd())}')
# Split the file root and extension:
print(os.path.splitext(file_path))

# print(dir(os.path))
