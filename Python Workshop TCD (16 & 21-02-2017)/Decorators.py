"""
This module shows an example of using Decorators
"""
from functools import wraps


print("\n\n\nSimple Decorator\n")
# Simple decorator
def func_decorator(decorated_func):
	print("Inside the decorator...")
	def wrap(*args, **kwargs):
		print("Before function call")
		decorated_func(*args, **kwargs)
		print("After function call")
	return wrap

@func_decorator
def some_function(*args, **kwargs):
	print("Inside function")
	print("Args: ", args)
	print("Kwargs: ", kwargs)

some_function(10, 20, a=11, b=22)



print("\n\n\nComplex Decorator\n")
# With args
def func_decorator2(*fargs, **fkwargs):
	print("Inside the decorator...")
	print("Decorator args: ", fargs)
	print("Decorator kwargs: ", fkwargs)

	def wrap_dargs(decorated_func):
		def wrap(*args, **kwargs):
			print("Before function call")
			decorated_func(*args, **kwargs)
			print("After function call")
		return wrap
	return wrap_dargs


@func_decorator2('darg1', 'darg2', karg1='karg1', karg2='karg2')
def some_function(*args, **kwargs):
	print("Inside function")
	print("Args: ", args)
	print("Kwargs: ", kwargs)


some_function(10, 20, a=11, b=22)

