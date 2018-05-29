from abc import ABC, abstractmethod
from NameGenerator import GenName
import random

class Entity(ABC):
	@abstractmethod
	def onMessage(self, message):
		pass

class Physical(Entity):
	def __init__(self, name=None):
		self.name = name if name is not None else GenName().New()
		self.health = 100
		self.attack = 5
	def onMessage(self, message):
		if message.msgType == "damage":
			print("{0} deals {1} damage to {2}").format(message.msgFrom.name,message.msgData,message.msgTo.name)
			self.health -= message.msgData
		else:
			pass

class Hostile(Physical):
	def __init__(self):
		self.abilities = []

class Friendly(Physical):
	def __init__(self, recruitable=False, recruited=False):
		self.recruitable = recruitable
		self.recruited = recruited
		self.abilities = []
	def onMessage(self, message):
		if message.msgType == "damage":
			print("{0} deals {1} damage to {2}").format(message.msgFrom.name,message.msgData,message.msgTo.name)
			self.health -= message.msgData
		elif message.msgType == "recruit":
			if self.recruitable == True:
				self.recruited = True
		else:
			pass

class NonPhysical(Entity):
	def __init__(self):
		pass
		
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