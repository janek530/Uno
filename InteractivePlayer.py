from player import Player

class InteractivePlayer(Player):
    def choose_card_to_play(self, current_card):
        print(f"\n{self.name}, your hand: {', '.join(map(str, self.hand))}")
        print(f"current card on stack: {current_card}")

        playable_cards = [card for card in self.hand if
                          card.color == current_card.color or card.value == current_card.value or card.color == 'WILD' or current_card.color == 'WILD']

        if not playable_cards:
            print("you don't have any playable card!\ntakking from stack...")
            return None

        for id, card in enumerate(playable_cards, 1):
            print(f"{id}. {card}")

        while True:
            choice = input("Choose card to play (number) or press 'd' to take card from stack: ")
            if choice.lower() == 'd':
                return None
            elif choice.isdigit() and 1 <= int(choice) <= len(playable_cards):
                return playable_cards[int(choice) - 1]
            else:
                print("Incorrect input!")

    def set_color(self):
        colors = ['RED', 'BLUE', 'GREEN', 'YELLOW']

        for id, card in enumerate(colors, 1):
            print(f"{id}. {colors[id - 1]}")

        while True:
            choice = input("Choose color to set: ")
            if choice.isdigit() and 1 <= int(choice) <= 4:
                return colors[int(choice) - 1]
            else:
                print("Incorrect input!")