from PlayerInterface import PlayerInterface
from Card import Card
import random

class RandomPlayer(PlayerInterface):
    def card_choice(self, board: list) -> Card:
        return self.random_choice()

    def emergency_card_choice(self, board: list) -> Card:
        return self.card_choice(board)

    def map_choice(self, board: list):
        return board[0]

    def emergency_map_choice(self, board: list):
        return self.map_choice(board)
