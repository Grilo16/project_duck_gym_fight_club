class Duck:
    def __init__(self, name, attack, defense, speed, health, id = None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self._health = health
        self.id = id
        self.attacks = self.attacks_by_attack_pow()
        
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value
        if self._health < 0:
            self._health = 0
        
        return self._health
        
    
    def attacks_by_attack_pow(self):
        attacks = {"peck": 50}
        if self.attack > 50:
            attacks["wing attack"] = 69
        if self.attack > 100:
            attacks["gust"] = 100
        if self.attack > 200:
            attacks["DUCK MAXIMUM POWER"] = 999
        return attacks
    
    def ducky_attack(self, attack_name):
        return self.attacks[attack_name]
    
    def stat_up(self, gym_class):
        if gym_class.stat_up == "attack":
            self.attack += gym_class.stat_up_amount
        elif gym_class.stat_up == "defense":
            self.defense += gym_class.stat_up_amount
        elif gym_class.stat_up == "speed":
            self.speed += gym_class.stat_up_amount
        elif gym_class.stat_up == "health":
            self.health += gym_class.stat_up_amount
        