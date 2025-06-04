try:
    age=int(input("enter age:"))
    if age>17:
        if age%2==0:
            print("You are able to vote and your age is an even number.")
        else:
            print("You are able to vote and your age is an odd number.")
    else:
        print("You are not able to vote and your age is an odd number.")
except ValueError:
    print("Please enter number.")