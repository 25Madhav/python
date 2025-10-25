theboard={"7":" ","8":" ","9":" ",
          "4":" ","5":" ","6":" ",
          "1":" ","2":" ","3":" "}
board_keys=[]
for key in theboard:
    board_keys.append(key)

def printboard(board): 
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
    print("-----")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("-----")
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
    print("-----")

def game():
    turn="x"
    count=0
    for i in range(10):
        printboard(theboard)
        print("It is your turn," ,turn, ".Move to which place?")
        move=input()
        if theboard[move]==" ":
            theboard[move]=turn
            count+=1
        else:
            print("The place is already filled.\nMove to which place?")
            continue
        if count>=5:
            if theboard["7"]==theboard["8"]==theboard["9"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break
            elif theboard["4"]==theboard["5"]==theboard["6"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break    
            elif theboard["1"]==theboard["2"]==theboard["3"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break
            elif theboard["7"]==theboard["4"]==theboard["1"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break 
            elif theboard["8"]==theboard["5"]==theboard["2"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break       
            elif theboard["9"]==theboard["6"]==theboard["3"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break
            elif theboard["7"]==theboard["5"]==theboard["3"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break 
            elif theboard["9"]==theboard["5"]==theboard["1"]!=" ":
                printboard(theboard)
                print("\nGAME OVER\n")
                print(turn,"has won😀")
                break
        if count==9:
            print("The game has ended in a draw.")
        if turn=="x":
            turn="0"
        else:
            turn="x"
    a=(input("do you want to reset?Yes or no?"))
    if a=="Yes":
        game() 
    else:
        print("Thank you for playing." \
        "The game was made by Madhav.inc")
game()                   