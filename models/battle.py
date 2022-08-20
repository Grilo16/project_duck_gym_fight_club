class Battle:
    def __init__(self, duck_1, duck_2, id = None, winner = None):
        self.id = id
        self.duck_1 = duck_1
        self.duck_2 = duck_2
        self.winner = winner
        
    def fight_turn(self, duck_1_attack, duck_2_attack):
        if self.winner:
            return f"This battle is over {self.winner.name} won"
        if self.duck_1.health == 0:
            print("Duck 1 Cannot fight")
            return
        if self.duck_2.health == 0:
            print("Duck 2 Cannot fight")
            return
        
        self.duck_2.health -= self.duck_1.ducky_attack(duck_1_attack)
        
        if self.duck_2.health <= 0:
            self.winner = self.duck_1
            return "Game over" + self.duck_2.name
        self.duck_1.health -= self.duck_2.ducky_attack(duck_2_attack)
        
        if self.duck_1.health <= 0:
            self.winner = self.duck_2
            return "Game over" + self.duck_1.name
        
    def __str__(self):
        if self.winner == None:
            return "Fight is ongoing"
        return f"Winner was {self.winner.name}"
            
        