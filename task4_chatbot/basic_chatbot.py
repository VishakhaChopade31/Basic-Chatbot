"""
TASK 4: Basic Chatbot
CodeAlpha Python Programming Internship

A simple rule-based chatbot that responds to user inputs with predefined replies.

Features:
- Keyword-based response matching
- Multiple response variations
- Conversation history
- Graceful exit handling

Author: CodeAlpha Intern
"""

import random
from datetime import datetime

class SimpleChatbot:
    """A simple rule-based chatbot"""
    
    def __init__(self):
        """Initialize chatbot with response patterns"""
        self.name = "CodeAlpha Bot"
        self.conversation_history = []
        
        # Response patterns: {pattern: [possible responses]}
        self.responses = {
            # Greetings
            'hello': [
                "Hi! How can I help you today?",
                "Hello! Nice to meet you!",
                "Hey there! What's on your mind?",
                "Hi! Great to see you!"
            ],
            'hi': [
                "Hello! How are you doing?",
                "Hi there! How can I assist you?",
                "Hey! What brings you here today?"
            ],
            'hey': [
                "Hey! What's up?",
                "Hello! How can I help?",
                "Hi there! How are you?"
            ],
            
            # How are you
            'how are you': [
                "I'm doing great, thank you for asking! How about you?",
                "I'm fine, thanks! How are you today?",
                "I'm excellent! Hope you're doing well too!",
                "I'm just a bot, but I'm functioning perfectly! How are you?"
            ],
            'how do you do': [
                "I'm doing well! How about yourself?",
                "Great! How are things with you?"
            ],
            
            # Name questions
            'what is your name': [
                f"My name is {self.name}. What's yours?",
                f"I'm {self.name}, your friendly chatbot!",
                f"You can call me {self.name}!"
            ],
            'your name': [
                f"I'm {self.name}!",
                f"My name is {self.name}. Nice to meet you!"
            ],
            
            # Help
            'help': [
                "I'm here to chat with you! Try saying hello, asking how I am, or just have a conversation!",
                "I can respond to greetings, questions about myself, and general conversation. Just type anything!",
                "Need help? Just chat naturally with me! I understand basic questions and greetings."
            ],
            
            # Thank you
            'thank you': [
                "You're welcome!",
                "Happy to help!",
                "Anytime!",
                "No problem at all!"
            ],
            'thanks': [
                "You're welcome!",
                "Glad I could help!",
                "No worries!"
            ],
            
            # Goodbye
            'bye': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Take care!",
                "Goodbye! Come back soon!"
            ],
            'goodbye': [
                "Goodbye! It was nice chatting with you!",
                "See you next time!",
                "Take care! Goodbye!"
            ],
            'see you': [
                "See you later!",
                "Bye! See you soon!",
                "Take care!"
            ],
            
            # Small talk
            'good': [
                "That's great to hear!",
                "Wonderful!",
                "I'm glad things are good!",
                "That's fantastic!"
            ],
            'bad': [
                "I'm sorry to hear that. I hope things get better!",
                "That's unfortunate. Is there anything I can help with?",
                "I hope your day improves!"
            ],
            
            # About the bot
            'what can you do': [
                "I'm a simple chatbot! I can have basic conversations, answer questions about myself, and keep you company!",
                "I can chat with you, respond to your questions, and try to be helpful!",
                "I'm here to have a friendly conversation with you!"
            ],
            'who created you': [
                "I was created by a CodeAlpha intern as part of a Python programming project!",
                "A talented intern at CodeAlpha built me!",
                "I'm a project from the CodeAlpha internship program!"
            ],
            
            # Time
            'time': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                f"It's {datetime.now().strftime('%I:%M %p')} right now!"
            ],
            'date': [
                f"Today is {datetime.now().strftime('%B %d, %Y')}",
                f"The date is {datetime.now().strftime('%d/%m/%Y')}"
            ],
        }
        
        # Default responses for unknown inputs
        self.default_responses = [
            "I'm not sure I understand. Can you rephrase that?",
            "Interesting! Tell me more.",
            "I'm still learning. Could you say that differently?",
            "Hmm, I'm not quite sure how to respond to that.",
            "That's an interesting point! What else would you like to talk about?",
            "I'm a simple bot, so I might not understand everything. Try asking me something else!",
        ]
    
    def find_match(self, user_input):
        """Find matching pattern in user input"""
        user_input_lower = user_input.lower().strip()
        
        # Check for exact or partial matches
        for pattern, responses in self.responses.items():
            if pattern in user_input_lower:
                return random.choice(responses)
        
        # No match found
        return random.choice(self.default_responses)
    
    def chat(self, user_input):
        """Process user input and return response"""
        # Store in conversation history
        self.conversation_history.append({
            'timestamp': datetime.now(),
            'user': user_input,
            'bot': None
        })
        
        # Get response
        response = self.find_match(user_input)
        
        # Update history with response
        self.conversation_history[-1]['bot'] = response
        
        return response
    
    def is_goodbye(self, user_input):
        """Check if user wants to end conversation"""
        goodbye_words = ['bye', 'goodbye', 'exit', 'quit', 'see you']
        user_input_lower = user_input.lower().strip()
        return any(word in user_input_lower for word in goodbye_words)

def main():
    """Main function to run the chatbot"""
    print("\n" + "=" * 70)
    print("WELCOME TO CODEALPHA CHATBOT!")
    print("=" * 70)
    print("\nHello! I'm a simple chatbot. Type 'bye' or 'quit' to exit.")
    print("Try saying hello, asking how I am, or just chat with me!")
    print("-" * 70)
    
    # Create chatbot instance
    bot = SimpleChatbot()
    
    # Chat loop
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for empty input
        if not user_input:
            print(f"{bot.name}: Please say something!")
            continue
        
        # Get bot response
        response = bot.chat(user_input)
        print(f"{bot.name}: {response}")
        
        # Check if user wants to exit
        if bot.is_goodbye(user_input):
            print("\n" + "=" * 70)
            print("Thank you for chatting! Conversation ended.")
            print("=" * 70)
            break
    
    # Show conversation summary
    if len(bot.conversation_history) > 1:
        print(f"\nYou exchanged {len(bot.conversation_history)} messages in this conversation.")
        
        show_history = input("Would you like to see the conversation history? (yes/no): ").lower()
        if show_history in ['yes', 'y']:
            print("\n" + "=" * 70)
            print("CONVERSATION HISTORY")
            print("=" * 70)
            for entry in bot.conversation_history:
                print(f"\n[{entry['timestamp'].strftime('%H:%M:%S')}]")
                print(f"You: {entry['user']}")
                print(f"{bot.name}: {entry['bot']}")
            print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
