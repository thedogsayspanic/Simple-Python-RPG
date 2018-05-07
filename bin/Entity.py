from NameGenerator import GenName
import random

class Entity:
	def __init__(self, name=None):
		self.name = name if name is not None else GenName().New()
		self.health = 1
		self.attack = .05
	def onMessage(self, message):
		if message.msgType == "damage":
			print("{0} deals {1} damage to {2}").format(message.msgFrom,message.msgData,message.msgTo)
			self.health -= message.msgFrom.attack
		else:
			print("I dunno what that means...")

class Hostile(Entity):
	def __init__(self):
		self.abilities = []
		super().__init__()

class Friendly(Entity):
	def __init__(self, recruitable=False, recruited=False):
		self.recruitable = recruitable
		self.recruited = recruited
		self.abilities = []
		super().__init__()
	def onMessage(self, message):
		if message.msgType == "recruit":
			if self.recruitable == True:
				self.recruited = True

		
'''
	def attack_creature(self, Entity):
		damage = int(random.randint(round(self.attack*.5), round(self.attack*1.5)))
		if Entity.defenseAdvantage is True and (Entity.defense * 2) - damage < 0:
			print("%s attacks for %d damage.\n" % (self.name, damage))
			Entity.health = Entity.health + (Entity.defense * 2) - damage
			print("%s blocks for %d damage.\n" % (Entity.name, (Entity.defense * 2)))
			Entity.defenseAdvantage = False
		else:
			print("%s attacks for %d damage.\n" % (self.name, damage))
			Entity.health = Entity.health + Entity.defense - damage

	def defend(self):
		self.defenseAdvantage = True
		print("%s enters a defensive stance.\n" % (self.name))
'''