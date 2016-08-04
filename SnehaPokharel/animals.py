class Animals(object):
	def __init__(self, name, health): 
		self.health = health
		self.name = name
	
	def walk(self):
		print str(self.health - 1)
		return self 
    	
	def run(self): 
		print str(self.health - 5)
		return self 

	def displayHealth(self):
		print str(self.name)
		print str(self.health)
		return self 
		
class Dog(Animals):
	def __init__(self, name, health):
		super(Dog, self).__init__(name, health)
		self.health = 150
	def pet(self):
		print str(self.health + 5)
		return self 

class Dragon(Animals):
	def __init__(self, name, health=170):
		super(Dragon, self).__init__(name, health)
	def fly(self):
		print str(self.health - 10)
		return self 

#Commands below: 		
# Dragon1 = Dragon('Aragon')
# Dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
# Dog1 = Dog('Tom', 0)
# Dog1.walk().walk().walk().run().run().pet().pet().displayHealth()
# Animals1 = Animals('Pikachu', 100)
# Animals1.walk().walk().walk().run().run().displayHealth()

