from abc import ABCMeta, abstractmethod

class IComponent(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def notify(msg):
        """The reuqired notify method"""

    @staticmethod
    @abstractmethod
    def receive(msg):
        """The required receive method"""

class Component(IComponent):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    def notify(self, message):
        print(self.name + ": >>> Out >>> " + message)
        self.mediator.notify(message)

    def receive(self,message):
        print(self.name + "= <<< In <<< : " + message)

class Mediator():
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def notify(self, message):
        for _component in self.components:
            _component.receive(message)

MEDIATOR = Mediator()
COMPONENT1 = Component(MEDIATOR, "Component1")
COMPONENT2 = Component(MEDIATOR, "Component2")
COMPONENT3 = Component(MEDIATOR, "Component3")

COMPONENT1.notify("data")