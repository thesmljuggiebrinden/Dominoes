import random


class Pips:
    def __init__(self, number):
        self.count = number


class Side:
    def __init__(self, pip_value):
        self.pips = pip_value


class Domino:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return 'top: {}, bottom: {}'.format(
            self.top.pips.count, self.bottom.pips.count)


class Set:
    def __init__(self, size):
        self.set_of_dominoes = []

        for top in range(0, size + 1):
            for bottom in range(top, size + 1):
                top_side = Side(Pips(top))
                bottom_side = Side(Pips(bottom))
                new_domino = Domino(top_side, bottom_side)
                self.add(new_domino)

    def print_set(self):
        for domino in self.set_of_dominoes:
            print(domino)

    def add(self, domino):
        self.set_of_dominoes.append(domino)

    def scramble(self):
        random.shuffle(self.set_of_dominoes)


domino_set = Set(6)
domino_set.scramble()
domino_set.print_set()