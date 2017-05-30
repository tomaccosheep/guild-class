class Car(object):
	def __init__(self, color, number_of_doors):
		self.number_of_wheels = 4
		self.color = color
		self.number_of_doors = number_of_doors
	def __str__(self):
		return 'This {} car has {} wheels and {} doors.'.format(self.color, self.number_of_wheels, self.number_of_doors)
	def honk(self, times):
		for i in range(times):
			print('Honk!')


if __name__ == '__main__':
	print('This should be imported, not run')
