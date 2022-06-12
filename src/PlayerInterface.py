from Card import Card
import random

class PlayerInterface:
    def __init__(self, name: str):
        self.name = name
        self.cards = []
        self.played_value = []
        self.points = 0

    def card_choice(self, board: list):
        raise NotImplementedError("Player interface cannot make a card choice")

    def emergency_card_choice(self, board: list):
        raise NotImplementedError("Player interface cannot make an emergency card choice") # noqa

    def map_choice(self, board: list, player_cards: list, player_points: list) -> Card: # noqa
        raise NotImplementedError("Player interface cannot make a map choice")

    def emergency_map_choice(self, board: list) -> Card:
        return random.choice(board)

    def random_choice(self) -> Card:
        return random.choice(self.cards)

    def remove_card(self, card) -> int:
        try :
            idx = self.cards.index(card)
        except ValueError as e:
            return -1

        self.cards.pop(idx)
        return 0

    def add_point(self, points: int):
        self.points += points

    def add_played_value(self, value):
        self.played_value.append(value)

    def add_card(self, card):
        self.cards.append(card)
