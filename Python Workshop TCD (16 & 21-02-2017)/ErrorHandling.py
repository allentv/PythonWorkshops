"""
This module deals with error handling of code
"""
var_a = 10
var_b = 20

print("a/b : ", var_a / var_b)

var_b = 0


# Raises Error
# print("a/b : ", var_a / var_b)


print("\n\n\ntry-except-1\n")
try:
	print("a/b : ", var_a / var_b)
except Exception as e:
	print("Caught Exception!")


print("\n\n\ntry-except-2\n")
try:
	print("a/b : ", var_a / var_b)
except ZeroDivisionError as e:
	print("In specific Error handler:\n", e)
except Exception as e:
	print("Caught Exception!")


var_b = 1

print("\n\n\ntry-except-else\n")
try:
	print("a/b : ", var_a / var_b)
except ZeroDivisionError as e:
	print("In specific Error handler:\n", e)
else:
	print("No Error!!!")


var_b = 0
print("\n\n\ntry-except-finally\n")
try:
	print("a/b : ", var_a / var_b)
except Exception as e:
	print("Caught Exception!")
finally:
	print("In finally block...")


var_b = 1
print("\n\n\ntry-except-else-finally\n")
try:
	print("a/b : ", var_a / var_b)
except ZeroDivisionError as e:
	print("In specific Error handler:\n", e)
else:
	print("No Error!!!")
finally:
	print("In finally block...")
