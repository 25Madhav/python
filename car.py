class bmw:
    def fuel(self):
        print("The fuel of a bmw is 120L.")
    def max_speed(self):
        print("The max speed of a bmw is 150mph.")
class ferrari:
    def fuel(self):
        print("The fuel of a ferrari is 140L.")
    def max_speed(self):
        print("The max speed of a ferrari is 160mph")
obj_bmw=bmw()
obj_ferrari=ferrari()
for car in (obj_bmw,obj_ferrari):
    car.fuel()
    car.max_speed()