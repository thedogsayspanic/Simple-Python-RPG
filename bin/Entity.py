from NameGenerator import GenName
import random

class Entity:
	def __init__(self, name=None, health=100, attack=10, attackAdvantage=False, defense=10, defenseAdvantage=False):
		self.name = name if name is not None else GenName().New()
		self.health = health
		self.attack = attack
		self.attackAdvantage = attackAdvantage
		self.defense = defense
		self.defenseAdvantage = defenseAdvantage

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