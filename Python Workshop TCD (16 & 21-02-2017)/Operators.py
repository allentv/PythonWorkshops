"""
Example of different operators in Python
"""

# Arithmetic Operators
print("\n\n\n===== Integer =====\n")
a_int = 2

print("Number : ", a_int)
print("\n")

print("Adding 2		: ", a_int + 2)
print("Subtracting 2		: ", a_int - 2)
print("Multiplying by 2	: ", a_int * 2)
print("Dividing by 2		: ", a_int / 2)
print("Raising by 2		: ", a_int ** 2)

print("\nChecking Integer type	: {}\n".format(type(a_int) is int))

print("\nAssignment Operators : +=, -=, /=, *=, **=\n")
a_int += 2
print("Adding 2	: ", a_int)

a_int -= 2
print("Subtracting 2	: ", a_int)

a_int /= 2
print("Dividing 2	: ", a_int)

a_int *= 2
print("Multiplying 2	: ", a_int)

a_int **= 2
print("Raising 2	: ", a_int)

print("\n\nChecking Integer type	: {}".format(type(a_int) is int))
print("\nChecking Floating type	: {}".format(type(a_int) is float))


print("\n\n\n===== Boolean =====\n")
a_bool = True

print("Boolean : ", a_bool)
print("\n")

print("True		: ", a_bool)
print("False		: ", not a_bool)


print("\n\n\n===== Comparison =====\n")
print("Is 4 > 2 ?	: ", (4 > 2))
print("Is 4 < 2 ?	: ", (4 < 2))
print("Is 4 != 2 ?	: ", (4 != 2))
print("Is 4 == 2 ?	: ", (4 == 2))
print("Is 4 >= 4 ?	: ", (4 >= 4))
print("Is 4 <= 5 ?	: ", (4 <= 5))
