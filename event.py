class Event:
    _events = {}

    def on(eventName, eventFunction):
        try:
            Event._events[eventName].append(eventFunction)
        except KeyError:
            Event._events[eventName] = []
            Event._events[eventName].append(eventFunction)

    def emit(eventName):
        try:
            [fn() for fn in Event._events[eventName]]
        except:
            raise KeyError('Event not found.')

class CollideEvent(Event):
    pass

class KeyEvent(Event):
    pass
