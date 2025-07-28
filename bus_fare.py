class vehicle:
    def __init__(self,seats,price):
        self.seats=seats
        self.price=price
    def bill (self):
        print("There are",self.seats,"seats.")
        print("Your bill is",self.price,".")
class bus(vehicle):
    def __init__(self, seats, price):
        vehicle.__init__(self,seats,price)
obj=bus(100,"£5")
obj.bill()