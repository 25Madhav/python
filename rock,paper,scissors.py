import random
print("1=rock,2=paper,3=scissors.")
a=int(input("enter choice:"))
b=random.randint(1,3)
print("the computer has chosen",b,".")
if a==1 and b==3:
    print("You win.")
elif a==2 and b==3:
    print("You lose.")
elif a==2 and b==1:
    print("You win.")
elif a==3 and b==1:
    print("You lose.")
elif a==1 and b==2:
    print("You lose.")
elif a==3 and b==2:
    print("You win")
else:
    print("You tied.")