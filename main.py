import game_class
import game_object
import player_object
import trigger_object

def start_game(game):
    player_object.player(game=game,texture="default_animated.png",animated=True)


if __name__ == "__main__":
    game = game_class.game()
    start_game(game)
    game.game_loop()