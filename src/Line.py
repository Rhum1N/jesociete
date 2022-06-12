from Card import Card


class Line:
    def __init__(self, card: Card, max_card: int):
        self.max_card = max_card
        self.cards = [None] * max_card
        self.cards[0] = card

    def get_nb_cards(self):
        nb_card = 0
        for c in self.cards:
            if c is None:
                return nb_card
            else:
                nb_card += 1

        return nb_card
        
    def get_total_point(self):
        point = 0
        for i in range(self.get_nb_cards()):
            point += self.cards[i].get_point()

        return point

    def get_line(self):
        return self.cards

    def insert_card(self, card: Card) -> int:
        nb_card = self.get_nb_cards(self)

        # when adding last card into line
        # return total value of line and re init cards
        if nb_card == self.max_card - 1:
            value = self.get_total_point()
            self.cards = [None] * self.max_card
            self.cards[0] = card
            return value

        self.cards[nb_card] = card
        return 0

    def get_last_value():
        nb_card = self.get_nb_cards()
        return self.cards[nb_card-1].get_value()
