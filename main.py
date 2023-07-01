import game_class
import player_object
import gui



if __name__ == "__main__":
    
    
    game = game_class.game()
    gui.MainMenu(game)
    game.game_loop()