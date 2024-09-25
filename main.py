from game import Game
from InteractivePlayer import InteractivePlayer
from player import Player

if __name__ == "__main__":
    player_names = ["Bot1", "Bot2", "Bot3"]
    players = [InteractivePlayer("You")]
    players += [Player(name) for name in player_names]
    game = Game(players)
    game.start_game()