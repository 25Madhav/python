class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
    flash=[]
    print("welcome to flashcard app")
    while(True):
        word=input("Enter a word:")
        meaning=input("enter a meaning:")
        flash.append(flashcard(word,meaning))
        option=int(input("enter 0 otherwise enter 1 to add another flashcard"))
        if option==0:
            break
    print("your flashcards")
    for i in flash:
        print(i)