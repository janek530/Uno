from stack import Stack
from player import Player

class Game:
    def __init__(self, players):
        self.stack = Stack()
        self.players = players
        self.current_player_id = 0
        self.current_card = self.stack.draw_card()
        self.direction = 1

        for player in self.players:
            player.draw(self.stack, 7)

    def play_turn(self):
        self.stack.show_stack()
        current_player = self.players[self.current_player_id]
        print(f"{current_player.name}'s turn. Current card: {self.current_card}")

        if current_player.has_playable_card(self.current_card):
            card_to_play = current_player.choose_card_to_play(self.current_card)
            if card_to_play:
                current_player.play_card(card_to_play)
                self.current_card = card_to_play
                print(f"{current_player.name} zagrał {card_to_play}")
            else:
                current_player.draw(self.stack)
                print(f"{current_player.name} dobrał kartę.")
        else:
            current_player.draw(self.stack)
            print(f"{current_player.name} dobrał kartę, brak możliwych zagrań.")

        # Sprawdź, czy gracz wygrał
        if not current_player.hand:
            print(f"{current_player.name} wins!")
            return True

        # Zmiana tury
        self.current_player_id = (self.current_player_id + self.direction) % len(self.players)
        return False

    def start_game(self):
        game_over = False
        while not game_over:
            game_over = self.play_turn()