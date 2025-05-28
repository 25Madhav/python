a=int(input("enter number:"))
def cube(b):
    print("the cube is",b*b*b)

def d3(c):
    if c%3==0:
        cube(c)
d3(a)