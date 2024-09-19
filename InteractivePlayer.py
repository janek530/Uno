from player import Player

class InteractivePlayer(Player):
    def choose_card_to_play(self, current_card):
        """Interaktywny wybór karty przez użytkownika."""
        print(f"\n{self.name}, twoja ręka: {', '.join(map(str, self.hand))}")
        print(f"Obecna karta na stole: {current_card}")

        playable_cards = [card for card in self.hand if
                          card.color == current_card.color or card.value == current_card.value or card.color == 'WILD']

        if not playable_cards:
            print("Nie masz żadnej pasującej karty.")
            return None

        # Wyświetl dostępne karty do zagrania
        for idx, card in enumerate(playable_cards, 1):
            print(f"{idx}. {card}")

        while True:
            choice = input("Wybierz kartę do zagrania (numer) lub wpisz 'd', aby dobrać kartę: ")
            if choice.lower() == 'd':
                return None  # Gracz decyduje się dobrać kartę
            elif choice.isdigit() and 1 <= int(choice) <= len(playable_cards):
                return playable_cards[int(choice) - 1]
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")