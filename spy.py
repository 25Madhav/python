import colorama
from colorama import Fore,Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to sentiment spy!{Style.RESET_ALL}").strip()
username=input(f"{Fore.MAGENTA}Please enter your name:{Style.RESET_ALL}").strip()
if not username:
    username="Mystery Agent"
conversation_history=[]
print(f"\n{Fore.CYAN}Hello Agent{username}!")
print(f"Type a sentence and using textblob I will analyze your sentences and telll you your sentiment.")
print(f"Type {Fore.YELLOW}'resset'{Fore.CYAN},{Fore.YELLOW}'history'{Fore.CYAN},"
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")
while True:
    user_input=input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower()=="exit":
        print(f"\n{Fore.BLUE}Exiting sentiment spy.Farewell Agent {username}!{Style.RESET_ALL}")
        break
    elif user_input.lower()=="rest":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower()=="history":
        if not conversation_history:
            print(f"{Fore.YELLOW}no conversation history yet:{Style.RESET_ALL}")
        else:    
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx,(text,polarity,sentiment_type) in enumerate(conversation_history,start=1):
                if sentiment_type=="Positive":
                    color=Fore.GREEN
                elif sentiment_type=="Negative":
                    color=Fore.RED
                else:
                    color=Fore.YELLOW
                print(f"{idx}. {color}{text}"
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue
    polarity=TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type="Positive" 
        color=Fore.GREEN
    if polarity < -0.25:
        sentiment_type="Negetive" 
        color=Fore.RED
    else:
        sentiment_type="Neutral"
        color=Fore.YELLOW
    conversation_history.append((user_input,polarity,sentiment_type))
    print(f"{color}{sentiment_type} Sentiment detected!"
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")