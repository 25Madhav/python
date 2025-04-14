math=int(input("enter your math score out of 100:"))
english=int(input("enter your english score out of 100:"))
computing=int(input("enter your coding score out of 100:"))
history=int(input("enter your history score out of 100:"))
art=int(input("enter your art score out of 100:"))
score=(math+english+computing+history+art)/5
if score>=90:
    print("you got an A.")
elif score>=80 and score<=90:
    print("you got a B.")
elif score>=70 and score<=80:
    print("you got a C")
elif score>=60 and score<70:
    print("you got a D")
elif score>=0 and score<=50:
    print("you fail.")