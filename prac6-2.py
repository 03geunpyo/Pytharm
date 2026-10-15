import math
import turtle
from figure import Polygon

class Triangle(Polygon):
    count = 0

    def __init__(self, sideLen):
        super().__init__(3, sideLen)
        Triangle.count += 1
        self.serial = Triangle.count

    def getArea(self):
        return (math.sqrt(3) / 4) * (self.sideLen ** 2)

    def getSerial(self):
        return self.serial

    def draw(self):
        for step in range(self.sideNumber):
            turtle.forward(self.sideLen)
            turtle.right(360 / self.sideNumber)
        input("Press any key to stop")

t1 = Triangle(300)
print(f"정삼각형 면적: {t1.getArea()}")
print(f"객체 번호(Serial): {t1.getSerial()}")
t1.draw()