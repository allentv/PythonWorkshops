"""
This module explores classes with added functionality in Python
"""
class Solid(object):
	def __new__(cls, *args, **kwargs):
		if hasattr(cls, 'obj_count'):
			cls.obj_count += 1
		else:
			cls.obj_count = 1
		return super(Solid, cls).__new__(cls)

	def __init__(self, length=1, width=2):
		self.length = length
		self.width = width

	def __str__(self):
		return "Length({}) & Width({})".format(self.length, self.width)

	@classmethod
	def count_of_objects(cls):
		return cls.obj_count

	@staticmethod
	def volume(length, width, height=10):
		return length * width * height

	def area(self):
		return self.length * self.width

	def square_length(self):
		return self.length ** 2

	def square_width(self):
		return self.width ** 2

	def __add__(self, obj):
		return Solid(
			length=self.length + obj.length,
			width=self.width + obj.width
		)

	def __sub__(self, obj):
		return Solid(
			length=self.length - obj.length,
			width=self.width - obj.width
		)

	def __mul__(self, obj):
		return Solid(
			length=self.length * obj.length,
			width=self.width * obj.width
		)

	def __truediv__(self, obj):
		return Solid(
			length=self.length / obj.length,
			width=self.width / obj.width
		)


if __name__ == '__main__':
	obj1 = Solid(11, 22)
	print('Object Count: ', Solid.count_of_objects())
	obj2 = Solid(10, 20)
	print('Object Count: ', Solid.count_of_objects())

	print('obj1 => Square Length: ', obj1.square_length())
	print('obj2 => Square Width: ', obj1.square_width())

	print('obj1 => Volume: ', obj1.volume(obj1.length, obj1.width))
	print('obj2 => Volume: ', obj2.volume(obj2.length, obj2.width))

	print('obj1 => Area: ', obj1.area())
	print('obj2 => Area: ', obj2.area())

	print('Add: ', obj1 + obj2)
	print('Subtract: ', obj1 - obj2)
	print('Multiply: ', obj1 * obj2)
	print('Divide: ', obj1 / obj2)

