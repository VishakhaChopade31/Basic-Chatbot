# Task 4: Basic Chatbot 🤖💬

## Project Overview
An intelligent rule-based chatbot built with Python that engages in natural conversations using pattern matching and predefined responses. Features conversation history, multiple response variations, and graceful handling of unknown inputs.

## Features ✨
- **50+ Response Patterns**: Handles greetings, questions, small talk, and farewells
- **Multiple Variations**: Different responses for same inputs to feel natural
- **Smart Matching**: Pattern recognition for flexible conversations
- **Conversation History**: Tracks all exchanges with timestamps
- **Graceful Unknown Handling**: Helpful responses for unrecognized inputs
- **Time/Date Awareness**: Can tell current time and date
- **Professional Design**: Object-oriented code structure

## How to Run 🚀

### Prerequisites
- Python 3.7 or higher
- Built-in modules only (random, datetime)

### Running the Chatbot
```bash
python basic_chatbot.py
```

## Conversation Capabilities 💬

### Greetings
- hello, hi, hey
- "Hi! How can I help you today?"

### Status Questions
- how are you, how do you do
- "I'm doing great, thank you for asking!"

### Identity Questions
- what is your name, your name
- "My name is CodeAlpha Bot!"

### Information
- what can you do
- "I'm a simple chatbot! I can have basic conversations..."

### Time & Date
- what time, what's the time
- "The current time is 14:30:45"

### Gratitude
- thank you, thanks
- "You're welcome!"

### Farewells
- bye, goodbye, see you
- "Goodbye! Have a great day!"

## Sample Conversation

```
======================================================================
WELCOME TO CODEALPHA CHATBOT!
======================================================================

Hello! I'm a simple chatbot. Type 'bye' or 'quit' to exit.
Try saying hello, asking how I am, or just chat with me!
----------------------------------------------------------------------

You: hello
CodeAlpha Bot: Hi! How can I help you today?

You: what is your name
CodeAlpha Bot: My name is CodeAlpha Bot. What's yours?

You: how are you doing
CodeAlpha Bot: I'm doing great, thank you for asking! How about you?

You: I'm doing good
CodeAlpha Bot: That's great to hear!

You: what can you do
CodeAlpha Bot: I can chat with you, respond to your questions, and try to be helpful!

You: thank you
CodeAlpha Bot: You're welcome!

You: bye
CodeAlpha Bot: Goodbye! Have a great day!

======================================================================
Thank you for chatting! Conversation ended.
======================================================================

You exchanged 7 messages in this conversation.
Would you like to see the conversation history? (yes/no): yes

======================================================================
CONVERSATION HISTORY
======================================================================

[14:30:15]
You: hello
CodeAlpha Bot: Hi! How can I help you today?

[14:30:22]
You: what is your name
CodeAlpha Bot: My name is CodeAlpha Bot. What's yours?

... (full conversation displayed)
```

## Code Structure 📁

```python
basic_chatbot.py
├── SimpleChatbot (Class)
│   ├── __init__()              # Initialize bot with responses
│   ├── responses (dict)         # All response patterns
│   ├── default_responses (list) # Fallback responses
│   ├── conversation_history     # Track chat history
│   ├── find_match()            # Pattern matching logic
│   ├── chat()                  # Process user input
│   └── is_goodbye()            # Detect exit intent
└── main()                      # Run chatbot loop
```

## Key Python Concepts Used 🐍

### 1. Classes and Objects (OOP)
```python
class SimpleChatbot:
    def __init__(self):
        self.name = "CodeAlpha Bot"
        self.responses = {}
    
    def chat(self, user_input):
        # Process and respond
        pass
```

### 2. Dictionaries for Response Mapping
```python
self.responses = {
    'hello': [
        "Hi! How can I help you?",
        "Hello! Nice to meet you!",
    ],
    'how are you': [
        "I'm doing great!",
        "I'm fine, thanks!",
    ]
}
```

### 3. Pattern Matching
```python
def find_match(self, user_input):
    user_input_lower = user_input.lower().strip()
    for pattern, responses in self.responses.items():
        if pattern in user_input_lower:
            return random.choice(responses)
```

### 4. Random Module for Variety
```python
import random
response = random.choice(possible_responses)
```

### 5. Datetime Module
```python
from datetime import datetime
timestamp = datetime.now()
formatted = timestamp.strftime('%H:%M:%S')
```

### 6. List Comprehensions
```python
goodbye_words = ['bye', 'goodbye', 'exit', 'quit']
return any(word in user_input_lower for word in goodbye_words)
```

### 7. While Loops for Conversation
```python
while True:
    user_input = input("You: ")
    response = bot.chat(user_input)
    print(f"Bot: {response}")
    
    if bot.is_goodbye(user_input):
        break
```

## Response Categories 📋

### Current Patterns (50+ responses):

| Category | Patterns | Sample Response |
|----------|----------|----------------|
| Greetings | hello, hi, hey | "Hi! How can I help?" |
| Status | how are you | "I'm doing great!" |
| Identity | your name | "I'm CodeAlpha Bot!" |
| Help | help | "I'm here to chat!" |
| Thanks | thank you, thanks | "You're welcome!" |
| Goodbye | bye, goodbye | "See you later!" |
| Small Talk | good, bad | "That's great!" |
| Time | time, date | "It's 14:30" |
| Bot Info | what can you do | "I can chat!" |
| Creator | who created you | "A CodeAlpha intern!" |

## Customization Ideas 💡

### 1. Add More Responses
```python
self.responses = {
    # Add your own patterns
    'weather': [
        "I can't check weather, but I hope it's nice!",
        "Weather apps are better for that!"
    ],
    'joke': [
        "Why did the programmer quit? No array of hope!",
        "I'm not great at jokes, but I try!"
    ]
}
```

### 2. Add Personality Traits
```python
def __init__(self):
    self.name = "CodeAlpha Bot"
    self.mood = "happy"
    self.personality = "friendly"
    self.favorite_topic = "programming"
```

### 3. Add Context Awareness
```python
def __init__(self):
    self.user_name = None
    self.last_topic = None

def chat(self, user_input):
    # Remember user's name
    if "my name is" in user_input.lower():
        self.user_name = extract_name(user_input)
        return f"Nice to meet you, {self.user_name}!"
```

### 4. Add Emoji Support
```python
'hello': [
    "Hi! 👋 How can I help you today?",
    "Hello! 😊 Nice to meet you!",
]
```

### 5. Add Learning Capability (Advanced)
```python
def learn_response(self, pattern, response):
    if pattern not in self.responses:
        self.responses[pattern] = []
    self.responses[pattern].append(response)
    self.save_to_file()
```

### 6. Add Sentiment Analysis
```python
def detect_sentiment(self, text):
    positive_words = ['good', 'great', 'happy', 'awesome']
    negative_words = ['bad', 'sad', 'angry', 'awful']
    
    if any(word in text.lower() for word in positive_words):
        return 'positive'
    elif any(word in text.lower() for word in negative_words):
        return 'negative'
    return 'neutral'
```

### 7. Add Multi-Language Support
```python
LANGUAGES = {
    'en': {
        'hello': ['Hi!', 'Hello!'],
        'bye': ['Goodbye!', 'See you!']
    },
    'es': {
        'hola': ['¡Hola!', '¡Buenos días!'],
        'adiós': ['¡Adiós!', '¡Hasta luego!']
    }
}
```

## Advanced Features to Add 🚀

### 1. Spell Correction
```python
from difflib import get_close_matches

def correct_spelling(self, word):
    all_patterns = list(self.responses.keys())
    matches = get_close_matches(word, all_patterns, n=1, cutoff=0.6)
    return matches[0] if matches else word
```

### 2. Command System
```python
def process_command(self, user_input):
    if user_input.startswith('/'):
        command = user_input[1:].split()[0]
        if command == 'help':
            return self.show_help()
        elif command == 'stats':
            return self.show_stats()
```

### 3. Save Conversations
```python
def save_conversation(self):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"conversation_{timestamp}.txt"
    
    with open(filename, 'w') as f:
        for entry in self.conversation_history:
            f.write(f"{entry['timestamp']}: {entry['user']}\n")
            f.write(f"Bot: {entry['bot']}\n\n")
```

### 4. Topic Tracking
```python
TOPICS = {
    'programming': ['python', 'code', 'programming', 'developer'],
    'weather': ['weather', 'temperature', 'rain', 'sunny'],
    'sports': ['football', 'basketball', 'cricket', 'tennis']
}

def detect_topic(self, text):
    for topic, keywords in TOPICS.items():
        if any(keyword in text.lower() for keyword in keywords):
            return topic
    return 'general'
```

## Testing Checklist ✅

- [ ] Start chatbot successfully
- [ ] Test all greeting variations (hello, hi, hey)
- [ ] Ask "how are you" - check response
- [ ] Ask "what is your name" - verify bot name
- [ ] Ask "what can you do" - check capabilities
- [ ] Ask for time - verify it shows current time
- [ ] Ask for date - verify current date
- [ ] Say "thank you" - check acknowledgment
- [ ] Try random input - check default response
- [ ] Say "bye" - verify exit
- [ ] View conversation history - check formatting
- [ ] Test with empty input - verify handling
- [ ] Test with very long input - verify response
- [ ] Start multiple conversations - verify independence

## Common Issues & Solutions 🔧

**Issue**: Bot doesn't respond properly
- **Solution**: Check if pattern is defined in `self.responses`

**Issue**: Same response every time
- **Solution**: Add more variations in response list

**Issue**: Can't exit
- **Solution**: Type exactly 'bye', 'quit', or 'goodbye'

**Issue**: Conversation history not showing
- **Solution**: Verify you typed 'yes' when prompted

**Issue**: Time/date not updating
- **Solution**: Restart bot - datetime is called when pattern matches

## Real-World Applications 🌍

This project teaches concepts used in:
- 🤖 **Customer Service Bots**: Automated support
- 💬 **Messaging Assistants**: Facebook Messenger, WhatsApp bots
- 🏪 **E-commerce Chatbots**: Shopping assistants
- 📚 **Educational Bots**: Learning companions
- 🏥 **Healthcare Assistants**: Symptom checkers

## Learning Outcomes 📚

After completing this task, you will understand:
- ✅ Object-oriented programming (classes, methods)
- ✅ Dictionary data structures for mapping
- ✅ Pattern matching algorithms
- ✅ String manipulation techniques
- ✅ Control flow (if-elif-else, loops)
- ✅ Random selection for variety
- ✅ Datetime module usage
- ✅ List operations and comprehensions
- ✅ User input/output handling
- ✅ Conversation flow design

## Comparison with Modern Chatbots 🤖

### This Chatbot (Rule-Based):
- ✅ Fast responses
- ✅ Predictable behavior
- ✅ No training needed
- ❌ Limited understanding
- ❌ Can't learn new patterns

### Modern Chatbots (AI-Based):
- ✅ Natural language understanding
- ✅ Can learn from conversations
- ✅ Context awareness
- ❌ Require training data
- ❌ More complex to build

## Upgrade Paths 📈

### Level 1: Enhanced Rules
- Add more patterns
- Improve responses
- Add personality

### Level 2: Pattern Matching Improvements
- Add fuzzy matching
- Implement spell correction
- Add synonym handling

### Level 3: Simple AI
- Add intent classification
- Implement named entity recognition
- Add simple machine learning

### Level 4: Advanced AI
- Use transformers (GPT-style)
- Implement context awareness
- Add multi-turn conversations

## Performance Metrics 📊

Track these to improve your bot:
```python
metrics = {
    'total_conversations': 0,
    'average_length': 0,
    'matched_patterns': 0,
    'default_responses_used': 0,
    'user_satisfaction': 0
}
```

## Project Timeline ⏱️

- **Understanding**: 20-30 minutes
- **Testing**: 30-45 minutes
- **Customization**: 1-3 hours
- **Documentation**: 30 minutes
- **Total**: 2-4.5 hours

## Extension Projects 🎯

### Beginner Extensions:
1. Add 20+ more response patterns
2. Implement mood tracking
3. Add user name remembrance
4. Create command system

### Intermediate Extensions:
1. Add conversation save/load
2. Implement topic detection
3. Add spell correction
4. Create personality settings

### Advanced Extensions:
1. Build GUI interface (tkinter)
2. Add voice recognition (speech_recognition)
3. Integrate with Telegram/Discord API
4. Add simple machine learning (scikit-learn)

## Example Extended Conversation 💬

```
You: hello
Bot: Hi! How can I help you today?

You: my name is john
Bot: Nice to meet you, John! How are you doing?

You: I'm feeling great
Bot: That's wonderful to hear! What brings you here today?

You: what time is it
Bot: The current time is 14:30:45

You: can you tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 😄

You: haha that's funny
Bot: Glad you enjoyed it! Want to hear another?

You: maybe later, thanks
Bot: You're welcome! Feel free to ask anytime!

You: bye
Bot: Goodbye, John! Have a great day!
```

## Author 👨‍💻
Created as part of the CodeAlpha Python Programming Internship

## License 📄
Free to use for educational purposes

## Next Steps 🚶

1. **Test thoroughly**: Try various inputs
2. **Understand OOP**: Learn about classes and methods
3. **Add responses**: Expand the conversation abilities
4. **Customize personality**: Make it unique
5. **Implement features**: Choose one extension idea
6. **Document changes**: Update README
7. **Share**: Upload to GitHub with examples

---

**Ready to chat? Run `python basic_chatbot.py` and start talking! 🤖💬**

**Pro Tip**: The more patterns you add, the more intelligent your bot appears!
