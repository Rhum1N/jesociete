from Card import Card
import random


class Deck:
    """ Class to represents the deck (pioche in french)
    for cards generation during a pre game phase"""
    def __init__(self, nb_card: int):
        self.nb_card = nb_card
        self.cards = self._cards_generation(self.nb_card)
        self._shuffle()

    def _cards_generation(self, nb_card: int) -> list:
        cards = [Card(x) for x in range(1, nb_card+1)]
        return cards

    def get_card(self):
        card = self.cards.pop()
        return card

    def _shuffle(self):
        random.shuffle(self.cards)
