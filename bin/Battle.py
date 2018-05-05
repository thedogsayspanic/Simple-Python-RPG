from Entity import Entity

class Battle:
    def __init__(self, allies=[], opponents=[], environment=None, effect=None):
        self.allies = allies
        self.opponents = opponents
        self.environment = environment
        self.effect = effect