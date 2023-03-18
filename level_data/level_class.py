import texture_class
import json
class Level:
    def __init__(self,level_path) -> None:
        with open(level_path,"r") as data:
            self.level_data = json.load(data)
        for i in self.level_data["Data"]["Walls"]:
            print(i)

Level("level_data/level1.json")
    
