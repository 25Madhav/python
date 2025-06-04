try:
    age=int(input("enter age:"))
    if age>17:
        print("You are able to vote.")
    else:
        print("You are not able to vote.")
except ValueError:
    print("Please enter number.")