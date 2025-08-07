from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run.")
class dog(animal):
    def move(self):
        print("I can bark")
obj=human()
obj.move()
obj=dog()
obj.move()