from random import choice

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
        
        if self.first_attacker() == "duck_1": 
            self.duck_1_attack(duck_1_attack)
            check_winner = self.check_winner()
            if check_winner:
                return 
            self.duck_2_attack(duck_2_attack)
            check_winner = self.check_winner()
            if check_winner:
                return 
            return
        
        elif self.first_attacker() == "duck_2": 
            self.duck_2_attack(duck_2_attack)
            check_winner = self.check_winner()
            if check_winner:
                return 
            self.duck_1_attack(duck_1_attack)
            check_winner = self.check_winner()
            if check_winner:
                return 
            return
        
    def duck_1_attack(self, attack):
        duck_1_damage = max(self.duck_1.ducky_attack(attack) - self.duck_2.defense, 0)
       
        self.duck_2.health -= duck_1_damage
    
    def duck_2_attack(self, attack):
        duck_2_damage = max(self.duck_2.ducky_attack(attack) - self.duck_1.defense, 0)
       
        self.duck_1.health -= duck_2_damage
  
    def check_winner(self):    
        if self.duck_1.health <= 0:
            self.winner = self.duck_2
            return True
        elif self.duck_2.health <= 0:
            self.winner = self.duck_1
            return True
        return False
    
    def first_attacker(self):
        speed_compare = [1, 2]
        for _ in range(self.duck_1.speed):
            speed_compare.append(1)
        for _ in range(self.duck_2.speed):
            speed_compare.append(2)
        if choice(speed_compare) == 1:
            return "duck_1"
        elif choice(speed_compare) == 2:
            return "duck_2"
        
    
    
    def __str__(self):
        if self.winner == None:
            return f"Fight is ongoing {self.duck_1.name} health is {self.duck_1.health} and {self.duck_2.name} health is {self.duck_2.health}"
        return f"Winner was {self.winner.name}"
            
        