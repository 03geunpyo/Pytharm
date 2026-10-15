from abc import ABC, abstractmethod

class Polygon(ABC):
    def __init__(self, sideNumber, sideLen):
        self.sideNumber = sideNumber
        self.sideLen = sideLen

    @abstractmethod
    def getArea(self):
        pass

class Triangle(Polygon):
    def __init__(self, sideLen):
        super().__init__(3, sideLen)

    def getArea(self):
        import math
        return (math.sqrt(3) / 4) * (self.sideLen ** 2)