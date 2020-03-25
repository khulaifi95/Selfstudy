# Boolean values: True, False

a = 3
b = 5

# Comparison
a == b 	# False
a != b 	# True

# Inequality
a > b 	# False
a < b 	# True

type(True)	# type 'bool'

bool(28)	# True
bool(-2)	# True
bool(0)		# False
bool("Turing")	# True
bool("")	# False

# Boolean conversions: trivial -> False, non-trivial -> True

str(True)	# 'True'
str(False)	# 'False'

int(True)	# 1
int(False)	# 0

5 + True	# 6
10 * False	# 0