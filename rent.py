from card import Card

class Rent(Card):

    def setColors(self, colors = []):
        return "colors " + colors.__str__()
