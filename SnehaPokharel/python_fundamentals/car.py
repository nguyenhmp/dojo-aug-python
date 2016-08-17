class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.tax = 0
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage	

	def display_all(self):
		print 'Price:' + str(self.price)
		print 'Speed:' + str(self.speed) + ' mph'
		print 'Fuel:' + str(self.fuel)
		print 'Mileage:' + str(self.mileage) + ' mpg'
		if self.price > 10000:
			print 'Tax:' + '.15'
		elif self.price < 10000:
			print 'Tax:' + '.12'


car1 = Car(2000, 35, 'Full', 105)
car1.display_all()

car2 = Car(2000, 5, 'Not Full', 105)
car2.display_all()

car3 = Car(2000, 15, 'Kind of Full', 95)
car3.display_all()

car4 = Car(2000, 25, 'Full', 25)
car4.display_all()

car5 = Car(20000, 35, 'Empty', 15)
car5.display_all()