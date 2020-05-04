# Operations: + - * /

x = 28	# int
y = 28.0	# float
float(28)	# 28.0
int(3.14)	# 3

# ints are narrower than floats
# floats are wider than ints

m = 1.732	# float
n = 1.732 + 0j	# complex
complex(m)	# 1.732 + 0j
float(n)	# ERROR

# floats are narrower than complex numbers
# complex numbers are wider than floats

a = 2	# int
b = 6.0	# float
c = 12 + 0j	# complex number

# Rule: Widen numbers so they're the same type

# 1) Addition
a + b	# 8.0 float

# 2) Subtraction
b - a 	# 4.0 float

# 3) Multiplication
a * 7	# 14 int

# 4) Division
c / b	# 2 + 0j complex

16 % 5	# mod
16 // 5	# quotient