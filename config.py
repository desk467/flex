from flex.frontend import *
from flex.internals import Vector

class Configuration:
    _frontend = SDLFrontend
    _title  = 'flex game'
    _width, _height = Vector(640, 480)

    def setFrontend(frontendClass):
        _frontend = frontendClass

    def setTitle(title):
        _title = title

    def setSize(size):
        _width, _height = size
