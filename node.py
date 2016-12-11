from flex.internals import Vector
from flex.tag import Tag

class Node:
    _instances = {}
    _tags = {}

    def __init__(self, name):
        self.name = name
        self._instances[name] = self

    def __repr__(self):
        return "{}(name = '{}')".format(__class__.__name__, self.name)

    def tag(self, tagName, tagParams=()):
        self._tags[tagName] = Tag(tagName)

class AnonymousNode(Node):
    def __init__(self):
        Node.__init__(self, __class__.__name__)

class SpriteNode(Node):
    def __init__(self, name, position, image, size=(None, None)):
        Node.__init__(self, name)
        self.position = Vector(*position)
        self.size = Vector(*size)

class TextNode(Node):
    def __init__(self, name, position, text=None, bind=None):
        Node.__init__(self, name)
        self.position = Vector(*position)
        self.text = text
        self.bind = bind

class SoundNode(Node):
    pass
