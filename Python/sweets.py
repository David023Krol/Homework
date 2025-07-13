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
            print(f"{s.getTypeOf()}: {s.getKindOf()}")

    def createSweets(self, type_of, kind_of, number = 1):

        if kind_of == "Pralines":
            for i in range(number):
                self.__sweets.append(Pralines(type_of))
        
        elif kind_of == "Truffles":
            for i in range(number):
                self.__sweets.append(Truffles(type_of))

sweets = Factory()
sweets.createSweets("Pralines", "Chocolate", 3)
sweets.createSweets("Truffles", "nougat", 2)
sweets.createSweets("Pralines", "Caramel", 1)
rum = Pralines("rum")
sweets.showProducts()
sweets.showDetails()
print(rum)