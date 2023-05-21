import game_class
import player_object
import gui

def start_game(game):
    player_object.player(game=game,texture="default/default_animated.png")


if __name__ == "__main__":
    
    
    game = game_class.game()
    start_game(game)
    gui.MainMenu(game)
    game.game_loop()