import random

class Character():
    def __init__(self, name, health, damage, attack_speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.attack_speed = attack_speed
        
    def attack(self,health_enemy):
        random_number = random.randint(0,7)
        if random_number == 0:
            print(f'{self.name} his attack failed')
        else:
            print(f'{self.name} performed a hit of {self.damage} damage')
            health_enemy -= self.damage
            
        
    def defend(self, damage_enemy):
        random_number = random.randint(0,7)
        if random_number == 0:
            print(f'{self.name} could not avoid the hit')
            self.health -= damage_enemy
        else:
            print(f'{self.name} successfully defended himself')
            
class Enemy(Character):
    pass

class Warrior(Character):
    pass

class Wizard(Character):
    pass

class Golem(Character):
    pass