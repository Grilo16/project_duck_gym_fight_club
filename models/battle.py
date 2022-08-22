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
        
        if self.round_attack_order() == "duck_1": 
            self.duck_1_attack(duck_1_attack)
            check_winner = self.has_winner()
            if check_winner:
                return 
            self.duck_2_attack(duck_2_attack)
            check_winner = self.has_winner()
            if check_winner:
                return 
            return
        
        elif self.round_attack_order() == "duck_2": 
            self.duck_2_attack(duck_2_attack)
            check_winner = self.has_winner()
            if check_winner:
                return 
            self.duck_1_attack(duck_1_attack)
            check_winner = self.has_winner()
            if check_winner:
                return 
            return
        
    def duck_attack(self, attacker_id, attack_name):

        if int(attacker_id) == self.duck_1.id:
            duck_1_damage = max(self.duck_1.ducky_attack(attack_name) - self.duck_2.defense, 0)
            self.duck_2.health -= duck_1_damage
            return self.duck_2
            
        elif int(attacker_id) == self.duck_2.id:
            duck_2_damage = max(self.duck_2.ducky_attack(attack_name) - self.duck_1.defense, 0)
            self.duck_1.health -= duck_2_damage
            return self.duck_1
        
            
    def duck_1_attack(self, attack):
        duck_1_damage = max(self.duck_1.ducky_attack(attack) - self.duck_2.defense, 0)
       
        self.duck_2.health -= duck_1_damage
    
    def duck_2_attack(self, attack):
        duck_2_damage = max(self.duck_2.ducky_attack(attack) - self.duck_1.defense, 0)
       
  
    def has_winner(self):    
        if self.duck_1.health <= 0:
            self.winner = self.duck_2
            return self.duck_2
        elif self.duck_2.health <= 0:
            self.winner = self.duck_1
            return self.duck_1
        return False
    
    def round_attack_order(self):
        speed_compare = [1, 2]
        for _ in range(self.duck_1.speed):
            speed_compare.append(1)
        for _ in range(self.duck_2.speed):
            speed_compare.append(2)
        if choice(speed_compare) == 1:
            return [self.duck_1, self.duck_2]
        elif choice(speed_compare) == 2:
            return [self.duck_2, self.duck_1]
        
    
    
    def __str__(self):
        if self.winner == None:
            return f"Fight is ongoing {self.duck_1.name} health is {self.duck_1.health} and {self.duck_2.name} health is {self.duck_2.health}"
        return f"Battle : {self.duck_1.name} VS {self.duck_2.name}|| Winner was {self.winner.name}"
            
        