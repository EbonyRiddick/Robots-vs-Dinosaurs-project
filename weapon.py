class Weapon:
    def __init__(self):
        self.name = ""
        self.attack_power = 0

    def weapon (self, weapon):
        if weapon == "1":
            self.name = 'Lightening Blade'
            self.attack_power = 20
        elif weapon == "2":
            self.name = 'Granade Launcher'
            self.attack_power = 10
        elif weapon == "3":
            self.name = 'Iron Fist'
            self.attack_power = 15
        
           