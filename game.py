from stack import Stack
from player import Player

class Game:
    def __init__(self, players):
        self.stack = Stack()
        self.players = players
        self.current_player_id = 0
        self.current_card = self.stack.draw_card()
        self.direction = 1
        self.count = 1

        for player in self.players:
            player.draw(self.stack, 7)

    def play_turn(self):
        current_player = self.players[self.current_player_id]
        print(f"{current_player.name}'s turn. Current card: {self.current_card}")
        if current_player.has_playable_card(self.current_card):
            card_to_play = current_player.choose_card_to_play(self.current_card)
            if card_to_play:
                current_player.play_card(card_to_play)
                self.current_card = card_to_play
                print(f"{current_player.name} played {card_to_play}")
                self.check_card(self.current_card, current_player)
            else:
                current_player.draw(self.stack, self.count)
                print(f"{current_player.name} taked card.")
        else:
            current_player.draw(self.stack, self.count)
            print(f"{current_player.name} taked card.")

        if not current_player.hand:
            print(f"{current_player.name} wins!")
            return True

        self.current_player_id = (self.current_player_id + self.direction) % len(self.players)
        return False

    def check_card(self, card, player):
        if card.value == 'COLOR':
            card.color = player.set_color()
        elif card.value == 'REVERSE':
            self.direction = self.direction * -1
        elif card.value == 'SKIP':
            if self.direction == 1:
                self.current_player_id = self.current_player_id + 1
            else:
                self.current_player_id = self.current_player_id - 1
        elif card.value == '+2':
            self.count = 2
            if self.direction == 1:
                self.current_player_id = self.current_player_id + 1
            else:
                self.current_player_id = self.current_player_id - 1
        elif card.value == '+4':
            self.count = 4
            card.color = player.set_color()
            if self.direction == 1:
                self.current_player_id = self.current_player_id + 1
            else:
                self.current_player_id = self.current_player_id - 1
        else:
            None

    def start_game(self):
        game_over = False
        while not game_over:
            game_over = self.play_turn()