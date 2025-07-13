from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def whoami(self):
        pass

class turtle(Animal):

    def whoami(self):
        print("I am a turtle")

class cat(Animal):

    def whoami(self):
        print("I am a cat")


t = turtle()
t.whoami()

c = cat()
c.whoami()