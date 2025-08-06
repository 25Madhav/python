class myclass:
    __privatevar=27
    def __privmeth(self):
        print("I am inside the class")
    def hello(self):
        print("privatevarible =",myclass.__privatevar)
obj=myclass()
obj.hello()
obj.__privmeth