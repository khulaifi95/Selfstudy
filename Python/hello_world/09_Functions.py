# Functions

def f():
	pass	# pass the line

dir()
# [... ,'f']

# 1. Return Values

def ping():
	return "Ping!"

ping()
# 'Ping!'

x = ping()
print(x)
# Ping!

import math

dir(math)
# ['pi']

# 2. Single Argument

def volume(r):
	"""Returns the volume of a sphere with radius r."""
	v = (4.0/3.0) * math.pi * r**3
	return v

volume(2)
# 33.5103

help(volume)
# volume(r)
# 		Returns the volume of a sphere with radius r.

# 3. Multiple Arguments

def triangle_area(b, h):
	"""Returns the area of a triangle with base b and height h."""
	return 0.5 * b * h

triangle_area(4, 5)
# 10

# 4. Keyword Arguments

def cm(feet = 0, inches = 0):
	"""Converts a length from feet and inches to centimeters."""
	inches_to_cm = inches * 2.54
	feet_to_cm = feet * 12 * 2.54
	return inches_to_cm + feet_to_cm

cm(feet = 5)
# 152.4

cm(inches = 70)

cm(inches = 10, feet = 10)

# 5. Multiple Types of Arguments: Keyword/ Required

def g(x = 0, y):
	return x + y
# SyntaxError: non-default argument follows default argument

def g(y, x = 0):
	return x + y

g(5)
# 5

g(7, x = 3)
# 10