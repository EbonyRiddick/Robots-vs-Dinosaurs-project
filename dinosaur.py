class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = 20
        self.health = 100

    def dino_name(self):
        self.name = input("Enter your dinosaur's name: ")
        print("You have chosen: ", self.name)

    def dino_attack(self, robot):
        self.attack_power -= robot 