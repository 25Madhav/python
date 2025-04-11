wheight=float(input("enter your wheight in kg:"))
height=float(input("enter your height in meters:"))
bmi=wheight/(height**2)
print(bmi)
if bmi<18.5:
    print("you are underweight.")
elif bmi>=18.5 and bmi<24.9:
    print("you are normal.")