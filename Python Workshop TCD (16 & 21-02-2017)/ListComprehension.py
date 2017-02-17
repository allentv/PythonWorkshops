"""
This module shows examples of list comprehension
"""

data = [1, 2, 3, 4, 5]
print("Actual data: ", data)

# List Comprehension
squared_list = [item ** 2 for item in data]
print("Squared data: ", squared_list)

# The above is equivalent to the below:
# squared_list = []
# for item in data:
# 	  squared_list.append(item ** 2)


# List Comprehension with an 'if' condition
odd_squares = [item ** 2 for item in data if item % 2 != 0]
print("Odd squares: ", odd_squares)

# The above is equivalent to the below:
# odd_squares = []
# for item in data:
# 	if item % 2 != 0
# 		odd_squares.append(item ** 2)


# List Comprehension with generator
squared_list = (item ** 2 for item in data)
print("Squared data (using Generator): ", squared_list)
print("Squared data (using Generator and typecast): ", list(squared_list))
