"""
This module deals with reading and writing to files
"""

# Creating a file
f = open('random_file_1.txt', 'w')
f.write('Some random text')
f.close()

# Using context generator
with open('random_file_2.txt', 'w') as f:
	f.write('Some random text')


# Writing a floating point number to file
abc = 123.456
with open('random_file_3.txt', 'w') as f:
	f.write(str(abc))

with open('random_file_3.txt', 'r') as f:
	print('String data from file: ', f.read())


# Persisting binary data
import pickle
with open('binary_data.txt', 'wb') as f:
	pickle.dump(abc, f)

with open('binary_data.txt', 'rb') as f:
	print('Pickle data from file: ', pickle.load(f))
