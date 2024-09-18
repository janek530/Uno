import numpy as np
from card import Card
class Cards:

    COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW']
    CARDS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'BLOCK', 'CHANGE', '+2']
    SPECIAL_CARDS = ['CHANGE_COLOR', '+4']

    def __init__(self):
        self.card_deck = []
        for color in self.COLORS:
            for card in self.CARDS:
                playing_card = Card(card, color)
                self.card_deck.append(playing_card)

        for _ in range(4):
            for card in self.SPECIAL_CARDS:
                self.card_deck.append(Card(card, None, 'special'))

        np.random.shuffle(self.card_deck)

    def get_deck(self):
        print(self.card_deck)

    def take_card(self):
        card = self.card_deck[0]
        self.card_deck.pop(0)
        return card
