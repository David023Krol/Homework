class Shape:
    def render(self):
        print("Initializing to render some shape...")

class square(Shape):
    def render(self):
        super().render()
        print("Rendering square...")

class triangle(Shape):
    def render(self):
        super().render()
        print("Rendering triangle...")

class circle(Shape):
    def render(self):
        super().render()
        print("Rendering circle...")

class pentagon(Shape):
    def render(self):
        super().render()
        print("Rendering pentagon...")

class Factory:

    __article = ["square", "triangle", "circle", "pentagon"]

    @staticmethod
    def create(represantative):

        if represantative in Factory.__article:
            return globals()[represantative]()
        else:
            return square()
        """
        match represantative:
            case "square":
                return square()
            case "square":
                return square()

            case "triangle":
                return triangle()

            case "circle":
                return circle()

            case "pentagon":
                return pentagon()
        
        """

        my_square = Factory.create("square")
        my_square.render()

        my_triangle = Factory.create("triangle")
        my_triangle.render()

        my_circle = Factory.create("circle")
        my_circle.render()

        my_pentagon = Factory.create("pentagon")
        my_pentagon.render()


class sweets:
    pass

class Pralines(sweets):
    
    def __init__(self, type_of):
        self.type_of = "Pralines"
        self.type_of = type_of

    def getTypeOf(self):
        return self.__type_of
    
    def getKindOf(self):
        return self.__kind_of
    
class Truffles(sweets):
    
    def __init__(self, type_of):
        self.type_of = "Truffles"
        self.type_of = type_of

    def getTypeOf(self):
        return self.__type_of
    
    def getKindOf(self):
        return self.__kind_of
    
class Factory:

    def __init__(self):
        self.__sweets = []

    def showProducts(self):
        print(f"available sweets: {self.__sweets}")

    def showDetails(self):
        for s in self.__sweets:
            print(f"{s.getTypeOf()} - {s.getKindOf()}")

    def createSweets(self, type_of, kind_of, number_of):

        if kind_of == "Pralines":
            self.__sweets.append(Pralines(type_of))
        
        elif kind_of == "Truffles":
            self.__sweets.append(Truffles(type_of))

        elif number_of == 0:
            print("There are no sweets available")

sweets = Factory()
sweets.createSweets("Chocolate", "Pralines", 3)
sweets.createSweets("nougat", "Truffles", 2)
sweets.createSweets("Caramel", "Pralines", 1)
rum = Pralines("rum")
sweets.showProducts()
sweets.showDetails()
print(rum)