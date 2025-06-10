import random
a=int(input("enter number from 1-100:"))
b=random.randint(1,100)
if a==b:
    print("The number you have chosen is the same as the computer.")
    print("The number the computer chose is",b,".")
else:
     print("The number you have chosen is not the same as the computer.")
     print("The number the computer chose is",b,".")

# print(random.choice("madhav"))
#write a code to generate a random number and match it with the input given by user.