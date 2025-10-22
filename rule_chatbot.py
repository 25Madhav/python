import random
import re
from colorama import Fore, Style, init

# Initialize colorama to enable colored text in the terminal.
# `autoreset=True` ensures the color resets after each print statement.
init(autoreset=True)

class TravelBot:
    """A rule-based chatbot for travel inquiries and jokes."""

    def __init__(self):
        # A list of jokes the bot can tell.
        self.jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "What do you call a fake noodle? An impasta!",
            "Did you hear about the restaurant on the moon? Great food, no atmosphere!"
        ]

        # A set of rules and responses using regex patterns.
        self.rules = {
            r'hi|hello|hey': [
                "Hello! Welcome to TravelBot. How can I help you plan your next adventure?",
                "Hey there! Ready to explore? Tell me about your travel plans.",
                "Greetings! I'm here to help you with your travel questions. What's on your mind?"
            ],
            r'plan.*trip|help.*plan|looking.*to travel': [
                "I can help with that! Where are you thinking of going?",
                "Fantastic! Let's get started. What's your dream destination?"
            ],
            r'.*recommendation|suggest.*place': [
                "There are so many great places! Do you prefer a beach, a city, or a mountain getaway?",
                "What kind of vacation do you have in mind? Relaxing, adventurous, or something in between?"
            ],
            r'.*budget.*|how.*much.*it cost': [
                "Travel costs can vary a lot. Can you give me a price range and a destination so I can give you a better idea?",
                "Tell me your budget, and I'll find some amazing options for you."
            ],
            r'best time to travel to (.*)': [
                "The best time to visit %s depends on what you want to do! Are you looking for good weather or to avoid crowds?",
                "For %s, the best time to go is usually during its off-peak season to save money."
            ],
            r'what about (.*)': [
                "Ah, %s! That's a great choice. What would you like to know about it?",
                "Tell me more about your interest in %s."
            ],
            r'tell me a joke': [self.get_joke],
            r'joke': [self.get_joke],
            r'thank|thanks': [
                "You're welcome! Is there anything else I can assist you with?",
                "My pleasure! Happy to help.",
                "Anytime! Feel free to ask if you need anything else."
            ],
            r'bye|goodbye|exit|quit': [
                "Goodbye! Enjoy your travels!",
                "Safe travels! Hope to chat again soon.",
                "Take care! Come back if you need any more travel tips."
            ],
            r'.*': [
                "I'm not sure I understand that. Can you rephrase?",
                "Sorry, I don't have information on that. Can we talk about travel or jokes instead?",
                "That's outside my travel expertise. Can you ask me a different question?"
            ]
        }

    def get_joke(self):
        """Returns a random joke from the jokes list."""
        return random.choice(self.jokes)

    def get_response(self, user_input):
        """Matches user input to a rule and generates a response."""
        user_input = user_input.lower()
        
        for pattern, responses in self.rules.items():
            match = re.match(pattern, user_input)
            if match:
                response = random.choice(responses)
                
                # Check if the response is a function (like get_joke)
                if callable(response):
                    return response()
                
                # Check for captured groups in the regex
                captured_groups = match.groups()
                if captured_groups:
                    # If the response template has a `%s`, insert the captured group.
                    return response % captured_groups
                else:
                    return response
        
        # This fallback is unlikely to be reached due to the `.*` catch-all rule,
        # but is good practice.
        return "I'm not sure how to respond to that."

    def chat(self):
        """The main chat loop."""
        print(f"{Fore.CYAN}TravelBot: Hello! I'm your travel buddy. I can help with travel plans and tell jokes. Type 'quit' to exit.")
        
        while True:
            user_input = input(f"{Fore.GREEN}You: ")
            
            if user_input.lower() in ('quit', 'exit', 'bye', 'goodbye'):
                print(f"{Fore.CYAN}TravelBot: {self.get_response(user_input)}")
                break
            
            response = self.get_response(user_input)
            print(f"{Fore.CYAN}TravelBot: {response}")

# Run the chatbot
if __name__ == '__main__':
    bot = TravelBot()
    bot.chat()