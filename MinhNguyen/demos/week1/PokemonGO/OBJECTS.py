class Player(object):
	def __init__(self, level=1, name="ash"):
		self.level = level
		self.name = name
		self.items = []
		self.pokemons = []
		self.six = []
		self.experience = 0
	def levelUp():
		self.level += 1
		#DO LATER
		# self.items.append()
		return self

class pokemon(object):
	def __init__(self, name, weight, combat_type, height, health, combat_point, evolve=True)
		self.name = name
		self.weight = weight
		self.combat_type = combat_type
		self.height = height
		self.health = health
		self.combat_point = combat_point
		self.evolve = evolve
		self.attacks = []
	def powerUp(self):
		self.combat_point += 10
	def evolve(self):
		if self.evolve:
			self.name = name
			self.weight = weight
			self.combat_type = combat_type
			self.height = height
			self.health = health
			self.combat_point = combat_point
			self.evolve = evolve
			return self
		else:
			return false

class AttackMove(object):
	def __init__(self, name, attack_point)
		self.name = name
		self.attack_point = attack_point
class Gym(object):
	def __init__(self, name, player):
		self.player = player
		self.name = name
		self.


