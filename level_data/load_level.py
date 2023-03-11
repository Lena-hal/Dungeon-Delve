
def read_level(level_name):
    with open(("level_data/"+level_name + ".lvl"), "r") as levelData:
        read_data = levelData.read()
        print(read_data)

read_level("level1")