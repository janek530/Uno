from card import Card

class Stack:

    last_card = ''

    def __init__(self, card):
        self.get_card(card)

    def get_card(self, card):
        self.last_card = card

    def print_card(self):
        return self.last_card
