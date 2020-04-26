def countdown(i):
    print(i)
    if i <= 0:	# base condition
        return
    else:		# iteration condition
        countdown(i - 1)

countdown(10)


def factorial(x):
	if x <= 0:
		return 0
	elif x == 1:
		return 1
	else:
		return x * factorial(x - 1)

print(factorial(10))