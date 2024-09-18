from gamer import Gamer

class Player(Gamer):

    def show_cards(self):
        counter = 0
        for i in self.deck:
            print(f"[{counter}] - {i}")
            counter += 1
        print(f"[{counter}] - pass")

    def play_card(self, num):
        if (num > len(self.deck)):
            return None
        card = self.deck[num]
        self.deck.pop(num)
        return card
