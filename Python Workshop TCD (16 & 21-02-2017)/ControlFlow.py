"""
This module showcases various control flow statements
"""

print("\n\n\nif\n")
if 2 > 1:
	print("2 > 1")


print("\n\n\nif-else\n")
if 2 < 1:
	print("2 < 1")
else:
	print("2 > 1")


print("\n\n\nif-elif-else\n")
if 2 < 1:
	print("2 < 1")
elif 2 == 2:
	print("2 == 2")
else:
	print("2 > 1")


print("\n\n\nwhile\n")
var_a = 1
total = 0
while var_a <= 10:
	total += var_a
	var_a += 1

print("Total Sum: ", total)


print("\n\n\nfor\n")
total = 0
for var_a in range(1, 11):
	total += var_a

print("Total Sum: ", total)
