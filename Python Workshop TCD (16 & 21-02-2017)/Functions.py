"""
This module shows examples of using Functions
"""

print("\n\n\nSimple Function\n")

# A simple function to compute sum of 2 numbers
def add(a, b):
	addition_result = a + b
	return addition_result

print("Sum of 1 and 2 is ", add(1, 2))


print("\n\n\nFunction with multiple return values\n")

# Return multiple values from a function
# Calculate the quotient and modulus for division of 2 numbers
def div_mod(a, b):
	bigger = max(a, b)
	smaller = min(a, b)
	div_result = bigger // smaller
	div_mod = bigger % smaller
	return div_result, div_mod

print("Division and Modulus : ", div_mod(10, 3))


print("\n\n\nAnonymous Function\n")

def square(x):
	return x * x

number_squared = lambda x: x * x

print("2 squared is ", number_squared(2))


print("\n\n\nFunctions with default arguments\n")

def func_default(a=1, b=2):
	print("Product of numbers is '{}'".format(a * b))

func_default()


print("\n\n\nFunctions with variable arguments\n")

def func_var_args(*args, **kwargs):
	print("Args are : ", args)
	print("Keyword Args are : ", kwargs)

	print("1st Arg : ", args[0])
	print("'b' Value : ", kwargs['b'])

func_var_args(10, 20, a=11, b=22)


def division(a, b, split=False):
	if split:
		return div_mod(a, b)
	return a / b


print(division(20, 10))
print(division(20, 10, split=True))
