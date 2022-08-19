class Duck:
    def __init__(self, name, attack, defense, health, id = None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.id = id
        
    def db_values(self):
        return [self.name, self.attack, self.defense, self.health]