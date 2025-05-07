a=int(input("enter number:"))
for b in range(2,a//2):
    if a%b==0:
        print("The number is not a prime number.")
        break
else:
    print("The numberb is a prime number.")