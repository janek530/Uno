import random

from cards import Card

class Stack:
    def __init__(self):
        self.cards = self.create_stack()
        random.shuffle(self.cards)


    def show_stack(self):
        print(len(self.cards))

    def create_stack(self):
        colors = ['RED', 'BLUE', 'GREEN', 'YELLOW']
        values = [str(i) for i in range(10)] + ['SKIP', 'REVERSE', '+2']
        stack = []

        for color in colors:
            for value in values:
                stack.append(Card(color, value))

        for _ in range(4):
            stack.append(Card('WILD', '+4'))
            stack.append(Card('WILD', 'COLOR'))

        return stack

    def draw_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            self.cards = self.create_stack()
            return None