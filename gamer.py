
class Gamer:

    deck = []

    def take_card(self, card):
        self.deck.append(card)

    def get_deck(self):
        return (self.deck)
