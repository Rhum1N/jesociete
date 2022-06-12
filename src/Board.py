from Card import Card
from Line import Line
from Deck import Deck


class Board:
    def __init__(self, nb_card: int, nb_line: int, nb_card_per_line: int, players: list, nb_card_per_player: int):
        self.nb_card = nb_card
        self.nb_line = nb_line
        self.max_card_line = nb_card_per_line
        self.nb_player_card = nb_card_per_player
        self.deck = Deck(nb_card)
        self.lines = [Line(self.deck.get_card(), nb_card_per_line) for _ in range(nb_line)]
        self.players = players
        self.distribute_cards()
        
    def run(self):
        for _ in range(self.nb_player_card):
            # lets player choose card
            played_cards = []
            for p in self.players:
                card = p.card_choice(self.lines)
                # TODO: handle timeout
                # TODO: handle cheat with abstract players
                # TODO: Add trace (csv or json)
                played_cards.append((p, card))
            # update board
            played_cards = sorted(played_cards, key=lambda x: x[1].get_value())
            for p, c in played_cards:
                value = self.add_card_to_line(c)
                # Player must select a line
                if value == -1:
                    line = p.map_choice(self.lines, None, None) # TODO: send data to players
                    p.add_point(line.insert_card(c))
                    # TODO: emergency map choice call
                    # TODO: timeout
                else:
                    p.add_point(value)
            
            # send data to players
            for p in self.players:
                for c, _ in played_cards:
                    p.add_played_value(c.get_value())

    def distribute_cards(self):
        for _ in range(self.nb_player_card):
            for p in self.players:
                card = self.deck.get_card()
                p.add_card(card)

    def add_card_to_line(self, card: Card):
        # find if card is lower than any line lower
        # find closer lower line
        # add card to line
        raise NotImplementedError("add card to line")
