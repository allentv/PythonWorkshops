"""
This module is an introduction to data structures - list, tuple, dict and set
"""

print("\n\n\n===== List =====\n")

data = [1, 2, 3, 4, 5]
print("List : ", data)


data = [1, 2, 3, 'a', 'b', 12.34]
print("List : ", data)


print("\n\n\n===== List Operations =====\n")

data = [1, 2, 3, 'a', 'b', 'c', 12.34, None]
print("Available Data : ", data)
print("\n")

print("No of items: ", len(data))

data.append([11, 12, 13])
print("After append: ", data)

print("Pop 1st element: ", data.pop(0))
print("Pop last element: ", data.pop())
print("After pop: ", data)

data.insert(0, 11)
print("After insert: ", data)

data.extend([11, 12, 13])
print("After extend: ", data)

print("Subset 2..5 => ", data[1:5])

data.reverse()
print("Reversed : ", data)
data.reverse()

print("Sorted : ", sorted([2, 34, 5, 1]))



print("\n\n\n===== Tuple Operations =====\n")
data = (1, 2, 3)
print("Data: ", data)
print("Number of elements: ", len(data))
print("2nd element: ", data[1])


print("\n\n\n===== Dictionary Operations =====\n")
data = {
	'key': 'value'
}
print("Data: ", data)
print("Accessing 'key': ", data['key'])

data['key1'] = 'value1'
data[1] = 1
print("Add 'key1' with 'value1' : ", data)

print("Check if 'key2' exists : ", data.get('key2', None))

print("All keys: ", data.keys())
print("All values: ", data.values())


