from abc import ABC, abstractmethod

class Polygon(ABC):
    """Abstraktní třída pro mnohoúhelník
    """

    @abstractmethod
    def numfsides(self):
        """Abstraktní metoda pro počet stran mnohoúhelníku
        """
        pass

class Triangle(Polygon):

    def numfsides(self):
        print("I have 3 sides")

class Pentagon(Polygon):

    def numfsides(self):
        print("I have 5 sides")

class Octagon(Polygon):

    def numfsides(self):
        print("I have 8 sides")

t = Triangle()
t.numfsides()

p = Pentagon()
p.numfsides()

o = Octagon()
o.numfsides()