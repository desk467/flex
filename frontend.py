class Frontend:
    def __init__(self, name):
        self.name = name

class SDLFrontend(Frontend):
    import sys
    import sdl2
    import sdl2.ext
    pass

class PygletFrontend(Frontend):
    pass

class PySFMLFrontend(Frontend):
    pass
