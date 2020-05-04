import os
from datetime import datetime

# Print out module dependencies
print(dir(os))

# Print out current directory
print(os.getcwd())

# Change to another directory
os.chdir('/home/kevinxu95/Desktop')
print(os.getcwd())
os.chdir('/home/kevinxu95/ACS/Selfstudy/Python_Tutorial')

# List all directories
print(os.listdir())

# Create a new directory
# os.mkdir('')	# only one level directory
# OR
os.makedirs('1/demo')

# Delete a directory
os.rmdir('1/demo')
# OR
# os.removedirs('../..')

# Rename a directory
os.rename('1', '2')

# Inspect stats of a file
mod_time = os.stat('10_Sets.py').st_mtime
print(datetime.fromtimestamp(mod_time))

# Traverse through the directory tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()):	# -> three value turple
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:', filenames)
	print()

# Print out the environment variable
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

# Separate file name and directory
print(os.path.split('/tmp/test.txt'))

# Check path
print(os.path.exists('/tmp/test.txt'))

# Split root and extension
print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))