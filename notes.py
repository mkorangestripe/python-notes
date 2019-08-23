# Sets the python path before running the shell:
# PYTHONPATH=./src ipython


# Convert between chr and int (integer ordinal):
ord('A') # 65
chr(65) # A
# Convert between hex and int
int(0x41) # 65
hex(65) # 0x41
# Convert between bin and int
int(0b1000001) # 65
bin(65) # 0b1000001
# Convert between oct and int
int(0101) # 65
oct(65) # 0101

# Multiple assignment:
a, b = 9, 2

# Return a list of valid attributes for the object:
dir(list)

# Use a global variable in a function:
global num



# copy
# Python creates a new object when the contents of a shallow copy are changed.
# The comparisons are value comparisons.
import copy
b = {1: [1,2,3]}

# Reference assignment (same object, same sub-objects)
a = b
id(a) # 4340438192
id(b) # 4340438192
id(a[1]) # 4340522520
id(b[1]) # 4340522520
a == b # True

# Shallow copy (new object, same sub-objects)
a = b.copy()
id(a) # 4340575600
id(b) # 4340438192
id(a[1]) # 4340522520
id(b[1]) # 4340522520
a == b # True
# This creates a new sub-object under 'a'.
a[1] = [4, 5, 6]
id(a[1]) # 4369444592
id(b[1]) # 4340522520
a == b # False
b[1] = [4, 5, 6]
a == b # True

# Deep copy (new object, new sub-objects)
a = copy.deepcopy(b)
a == b # True
id(a) # 4340489584
id(b) # 4340438192
id(a[1]) # 4340168608
id(b[1]) # 4340522520
a == b # True
