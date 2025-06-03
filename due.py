paid=int(input("enter amount paid:"))
bill=int(input("enter bill:"))
def due(paid,bill):
    print("the due amount is",bill-paid,"$")
due(paid,bill)