"""
This module is an example of how to implement a class.


A list is used as the underlying storage for a stack.
Values are added and removed from the start of the list.
"""
class Stack:
	# Constructor
	def __init__(self):
		self.items = []

	# Convert the object to a custom string representation
	def __str__(self):
		return str(self.items)

	# Remove the 1st element
	def pop(self):
		return self.items.pop(0)

	# Add an element to the beginning of a list
	def push(self, item):
		self.items.insert(0, item)

	# Remove all elements in the stack
	def flush(self):
		self.items = []

	# Get the number of elements in the stack
	def length(self):
		return len(self.items)

	# View the value at the top of the stack without removing it
	def peek(self):
		return self.items[0]


if __name__ == '__main__':
	# Create an object of class 'Stack'
	obj = Stack()

	# Push 3 values to the Stack
	obj.push(1)
	obj.push(2)
	obj.push('Three')

	print("Stack : ", obj)
	print("Number of elements : ", obj.length())
	print("Top value : ", obj.peek())
	print("Stack pop: ", obj.pop())
	print("Stack : ", obj)

	obj.flush()
	print("Flush : ", obj)
