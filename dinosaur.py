class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def dino_attack(self, robot):
        self.attack_power -= robot

    def dino_health(self):
        self.health = "health"

    def dino_name(self):
        self.name = dinosaurs

dinosaurs =[ 
        {
            "name": 'MegaSaurus Rex',
            "attack power": 10,
            "health": 100
        }

        {
            "name": 'Hulk',
            "attack power": 15,
            "health": 80
        }
  
        {
            "name": 'Godzilla',
            "attack power": 20,
            "health": 100
        }
    ]

    
      
