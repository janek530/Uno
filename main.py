import numpy as np
from cards import Cards
from player import Player
from stack import Stack

card_deck = Cards()
player = Player()
game_stack = Stack(card_deck.take_card())


for _ in range(5):
    player.take_card(card_deck.take_card())

while True:
    print(game_stack.print_card())



    player.show_cards()
    card_num = int(input("which card do you want to play? "))

    if card_num > len(player.get_deck()) - 1:
        player.take_card(card_deck.take_card())
    else:
        player.play_card(card_num)
    if len(player.deck) == 0:
        break
card_deck.get_deck()
