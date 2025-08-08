import random
class fruitquiz:
    def __init__(self):
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'yellow':'banana'}
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruit.items()))
            print("What is the color of{}".format(fruit))
            user_answer=input()
            if (user_answer.lower()==color):
                print("Correct answer.")
            else:
                print("Wrong answer.")
            option=int(input("enter 0 otherwise enter 1 to play again"))
            if (option):
                break
print("Welcome to fruit quiz")
fq=fruitquiz()
fq.quiz()