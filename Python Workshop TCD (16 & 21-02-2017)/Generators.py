"""
This module shows an example of using generator functions
"""

def series():
	for number in range(1, 11):
		yield number


print("Printing out the series of values from 1 to 10")
for num in series():
	print(num)
