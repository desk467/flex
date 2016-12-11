from flex.internals import Vector
from flex.config import Configuration

class Game:
    def __init__(self, name, size):
        Configuration.setSize(size)
        Configuration.setTitle(name)

    def addState(self, stateName, stateClass):
        pass

    def playState(self, stateName):
        pass

    def play(self):
        pass
