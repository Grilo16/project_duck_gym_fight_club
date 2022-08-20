class Battle:
    def __init__(self, duck1, duck2, id = None, winner = None):
        self.id = id
        self.duck1 = duck1
        self.duck2 = duck2
        self.winner = winner
        
    def fight_turn(self, duck1_attack, duck2_attack):
        if self.duck1.health == 0:
            print("Duck 1 Cannot fight")
            return
        if self.duck2.health == 0:
            print("Duck 2 Cannot fight")
            return
        
        self.duck2.health -= self.duck1.ducky_attack(duck1_attack)
        if self.duck2.health <= 0:
            self.winner = self.duck1.id
            return "Game over" + self.duck2.name
        self.duck1.health -= self.duck2.ducky_attack(duck2_attack)
        if self.duck1.health <= 0:
            self.winner = self.duck2.id
            return "Game over" + self.duck1.name
        
    def __str__(self):
        if self.winner == None:
            return "Fight is ongoing"
        return f"Winner is {self.winner}, {self.duck1.name} health is: {self.duck1.health}\n{self.duck2.name} health is: {self.duck2.health}"
            
            
        