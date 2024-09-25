import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.draw_card()
            if card:
                self.hand.append(card)

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        else:
            return None

    def has_playable_card(self, current_card):
        for card in self.hand:
            if card.color == current_card.color or card.value == current_card.value or card.color == 'WILD' or current_card.color == 'WILD':
                return True
        return False

    def choose_card_to_play(self, current_card):
        for card in self.hand:
            if card.color == current_card.color or card.value == current_card.value or card.color == 'WILD' or current_card.color == 'WILD':
                return card
        return None

    def set_color(self):
        return random.choice(['BLUE', 'GREEN', 'RED', 'YELLOW'])

    def __repr__(self):
        return self.name + ':' + str(self.hand)