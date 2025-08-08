class a:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if self.a < other.a:
            return"ob1 is less than ob2"
        else:
            return"ob2 is less than ob1"
    def __eq__(self,other):
        if self.a==other.a:
            return"ob1 is equal to ob2"
        else:
            return"not equal"
ob1=a(2)
ob2=a(3)
print("passed value:",ob1.a,ob2.a)
ob3=a(4)
ob4=a(4)
print("passed value:",ob3.a,ob4.a)
print(ob1 < ob2)
print(ob3==ob4)