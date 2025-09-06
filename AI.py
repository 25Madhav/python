from textblob import TextBlob
print("👋 Welcome to the AI Mood Detector!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Let's find out the sentiment of your sentences.")
print("Type 'exit' to quit.\n")
while True:
    sentence=input("enter sentence:")
    if sentence.lower()=="exit":
        print("Goodbye",{name})
        break
    blob=TextBlob(sentence)
    sentiment=blob.sentiment.polarity
    if sentiment >0:
        print("Positive sentiment detected!")
    elif sentiment <0:
        print("Negative sentiment detected!")
    else:
         print("Neautral sentiment detected!")