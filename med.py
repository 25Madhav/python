attendance=int(input("enter attendance number:"))
medical_cause=input("enter whether you have medical problem or not:")
if medical_cause=="yes":
    print("you can take the test.")
else:
    if attendance>75:
        print("you can take the test.")
    else:
        print("you can't take the test.")