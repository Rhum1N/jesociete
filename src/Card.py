class Card:
    """ Class for card representation.
    value is the number displayed on card while
    point are the point penalty given by card"""
    def __init__(self, value: int):
        self.value = value
        self.point = 0

        self._generate_point()

    def get_point(self):
        """ Returns penalties points hold by card"""
        return self.point

    def get_value(self):
        """ Returns displayed value"""
        return self.value

    def _generate_point(self):
        """ Generate penalty points and store it"""
        point = self._point_value_generation(self.value)
        self.point = point

    def _point_value_generation(self, value: int) -> int:
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

    def __str__(self):
        return str(self.get_value())

    def __repr__(self):
        return self.__str__()
