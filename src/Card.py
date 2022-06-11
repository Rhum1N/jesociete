class Card:
    """ Class for card representation.
    value is the number displayed on card while
    point are the point penalty given by card"""
    def __init__(self, value: int):
        self.value = value
        self.point = 0

        self.generate_point()

    def get_point(self):
        return self.point

    def get_value(self):
        return self.value

    def generate_point(self):
        point = _point_value_generation(self.value)
        self.point = point

    def _point_value_generation(value: int) -> int:
        """ Generates point of a card based on its value"""
        point = 0
        if value % 11 == 0:
            point += 5
        if value % 10 == 0:
            point += 3
        # get multiple of 5 that are not multiple of 10
        if (value - 5) % 10 == 0:
            point += 2

        return max(1, point)
