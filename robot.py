class Robot:
    def __init__(self, name):
        self.name = name
        self.health = ''
        self.weapons = []

    robot_one = {
        "first_name": 'Mega',
        "last_name" : 'Mental',
        "health": 100,
        "weapon" :[] 
    }
    
    robot_two = {
        "first_name": 'Iron',
        "last_name" : 'Man',
        "health": 87,
        "weapon" :[] 
    }

    robot_three = {
        "first_name": 'Elemental',
        "last_name" : 'Giant',
        "health": 125,
        "weapon" :[] 
    }
    robot_names = [robot_one, robot_two, robot_three]
    
    def robot_attack(self, dinosaur):
        self.weapons -= dinosaur 