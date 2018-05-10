import abc

class Card(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, value, title, description):
        self.title = title
        self.value = value
        self.description = description

    @abc.abstractmethod
    def setColors(self, colors = []):
        pass

    def __str__(self):
        return self.title + " $" + str (self.value) + "\n" + self.description
