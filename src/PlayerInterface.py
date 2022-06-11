from Card import Card
import random

class PlayerInterface:
    def __init__(self, name: str, cards: list):
        self.name = name
        self.cards = cards
        self.played_value = []

    def card_choice(self, board: list):
        raise NotImplementedError("Player interface cannot make a card choice")

    def emergency_card_choice(self, board: list):
        raise NotImplementedError("Player interface cannot make an emergency card choice") # noqa

    def map_choice(self, board: list, player_cards: list, player_points: list) -> Card: # noqa
        raise NotImplementedError("Player interface cannot make a map choice")

    def emergency_map_choice(self, board: list) -> Card:
        return random.choice(board)
