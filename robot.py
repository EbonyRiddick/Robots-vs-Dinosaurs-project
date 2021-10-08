from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = " "
        self.health = 100
        self.weapon = Weapon()
        self.still_kicking = True 

    def choose_weapon(self):
        pick_a_weapon = input(f"'
        \nPlease choose a weapon for {self.name}
        \n1: Lightening Blade")

    
    def robot_attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        if dinosaur.health <=0:
            dinosaur.still_kicking = False