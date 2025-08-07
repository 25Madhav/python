from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print("passed value",x)
    def task(self):
        print("we are inside the abc task class.")
class test_class(absclass):
    def task(self):
        print("we are inside the test class.")
obj=test_class()
obj.task()
obj.print(100)