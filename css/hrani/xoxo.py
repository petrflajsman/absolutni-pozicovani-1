class Place:
    def __init__(self, name, description, objects):
        self.name = name
        self.description = description
        self.objects = objects
        
    def __str__(self):
        return self.name


class Character:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location
        self.status = None
        
    def __str__(self):
        return self.name


# World Initialization
house = Place("House", "A small family house on the edge of the forest.", {"east": "Forest"})
forest = Place("Forest", "A dense forest with many trees.", {"west": "House", "north": "Dark Forest"})
dark_forest = Place("Dark Forest", "A dark and dangerous forest.", {"south": "Forest"})
    
house.objects["east"] = forest
forest.objects["west"] = house
forest.objects["north"] = dark_forest
dark_forest.objects["south"] = forest

player = Character("John", "A young man with a determination to explore the world.", house)

player.status = "Wakes up in the house and decides where to go next."

print(player.status)
print("Gets up from the bed and walks around the house.")
print("Leaves the house and enters the forest.")
player.location = forest
print("Observes the surrounding trees and ventures deeper into the forest.")
print("Suddenly feels lost and the darkness seems to be getting deeper.")
player.location = dark_forest
print("Tries to find a way back, but it seems like he is completely alone in the dark forest.")
