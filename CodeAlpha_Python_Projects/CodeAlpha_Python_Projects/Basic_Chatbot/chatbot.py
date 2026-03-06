# ============================================================
#  Basic Rule-Based Chatbot — CodeAlpha Python Internship
#  Task: Build a simple keyword-driven chatbot that responds
#        to common inputs with predefined replies.
# ============================================================

# ── Built-in imports ────────────────────────────────────────
import os
import random
import datetime


# ─────────────────────────────────────────────────────────────
#  RESPONSE LIBRARY
#  Each key is a category; the value is a list of possible
#  replies. The bot picks one at random for variety.
# ─────────────────────────────────────────────────────────────

RESPONSES = {

    # ── Greetings ────────────────────────────────────────────
    "greetings": [
        "Hey there! 😊 How can I help you today?",
        "Hello! Nice to meet you!",
        "Hi! I'm CodeBot — your friendly Python assistant. What's up?",
        "Hey! Great to see you. How's your day going?",
    ],

    # ── How are you ──────────────────────────────────────────
    "how_are_you": [
        "I'm doing great, thanks for asking! 😄",
        "All good on my end! Just waiting to chat. How about you?",
        "Feeling fantastic! Ready to help you out.",
        "Pretty good! Every conversation makes me smarter. 😄",
    ],

    # ── Name ─────────────────────────────────────────────────
    "name": [
        "I'm CodeBot 🤖 — built during the CodeAlpha Python Internship!",
        "My name is CodeBot. Powered by pure Python logic!",
        "They call me CodeBot. Nice to meet you!",
    ],

    # ── Help ─────────────────────────────────────────────────
    "help": [
        "Sure! Here's what I can talk about:\n"
        "  • Greetings (hello, hi, hey)\n"
        "  • How are you / status\n"
        "  • My name / who are you\n"
        "  • Time / date\n"
        "  • Jokes 😄\n"
        "  • Motivational quotes 💪\n"
        "  • Python tips 🐍\n"
        "  • Farewell (bye, exit, quit)\n"
        "\n  Type anything and I'll do my best!",
    ],

    # ── Time ─────────────────────────────────────────────────
    "time": [],     # filled dynamically in get_response()

    # ── Date ─────────────────────────────────────────────────
    "date": [],     # filled dynamically in get_response()

    # ── Jokes ────────────────────────────────────────────────
    "joke": [
        "Why do programmers prefer dark mode?\n"
        "  Because light attracts bugs! 🐛😄",
        "How many programmers does it take to change a light bulb?\n"
        "  None — that's a hardware problem! 💡",
        "I told my computer I needed a break.\n"
        "  Now it won't stop sending me Kit-Kat ads. 🍫",
        "Why was the JavaScript developer sad?\n"
        "  Because he didn't know how to 'null' his feelings. 😂",
        "A SQL query walks into a bar, walks up to two tables and asks...\n"
        "  'Can I join you?' 🍺",
    ],

    # ── Motivational quotes ───────────────────────────────────
    "motivation": [
        "💪 'The only way to do great work is to love what you do.' — Steve Jobs",
        "🚀 'Code is like humor. When you have to explain it, it's bad.' — Cory House",
        "🌟 'First, solve the problem. Then, write the code.' — John Johnson",
        "🔥 'Programs must be written for people to read, and only incidentally "
        "for machines to execute.' — Harold Abelson",
        "💡 'It always seems impossible until it's done.' — Nelson Mandela",
    ],

    # ── Python tips ───────────────────────────────────────────
    "python": [
        "🐍 Python Tip: Use list comprehensions for cleaner code!\n"
        "   squares = [x**2 for x in range(10)]",
        "🐍 Python Tip: Use `enumerate()` to get index + value in a loop!\n"
        "   for i, val in enumerate(my_list): ...",
        "🐍 Python Tip: Use f-strings for fast, readable string formatting!\n"
        '   name = "World"; print(f"Hello, {name}!")',
        "🐍 Python Tip: Use `zip()` to loop over two lists simultaneously!\n"
        "   for a, b in zip(list1, list2): ...",
        "🐍 Python Tip: The `get()` method on dicts avoids KeyError!\n"
        '   value = my_dict.get("key", "default")',
    ],

    # ── Weather (static reply — no API) ──────────────────────
    "weather": [
        "☀️ I wish I could check the weather, but I'm running offline!\n"
        "   Try weather.com or just look out the window. 😄",
    ],

    # ── Gratitude ────────────────────────────────────────────
    "thanks": [
        "You're welcome! 😊",
        "Happy to help! Anything else?",
        "Anytime! That's what I'm here for.",
        "My pleasure! 🙌",
    ],

    # ── Farewells ────────────────────────────────────────────
    "farewell": [
        "Goodbye! Have a wonderful day! 👋",
        "See you later! Keep coding! 💻",
        "Bye bye! Come back anytime. 😊",
        "Take care! Happy coding! 🐍",
    ],

    # ── Fallback ─────────────────────────────────────────────
    "fallback": [
        "Hmm, I'm not sure I understand. Try typing 'help' to see what I can do!",
        "I didn't quite catch that. Type 'help' for a list of topics!",
        "Interesting… but I'm not sure how to respond. Type 'help'!",
        "That's a bit beyond my current knowledge. Try 'help' for options!",
    ],
}


# ─────────────────────────────────────────────────────────────
#  KEYWORD → CATEGORY MAPPING
#  The bot checks each user input word-by-word against this
#  dictionary to decide which response category to use.
# ─────────────────────────────────────────────────────────────

KEYWORDS = {
    # Greetings
    "hello":      "greetings",
    "hi":         "greetings",
    "hey":        "greetings",
    "howdy":      "greetings",
    "sup":        "greetings",
    "hiya":       "greetings",
    "greetings":  "greetings",
    "good morning": "greetings",
    "good afternoon": "greetings",
    "good evening":   "greetings",

    # How are you
    "how are you": "how_are_you",
    "how r u":     "how_are_you",
    "how are":     "how_are_you",
    "feeling":     "how_are_you",
    "doing":       "how_are_you",

    # Name
    "name":        "name",
    "who are you": "name",
    "who r u":     "name",
    "what are you":"name",
    "your name":   "name",
    "yourself":    "name",

    # Help
    "help":        "help",
    "support":     "help",
    "what can":    "help",
    "commands":    "help",
    "options":     "help",
    "topics":      "help",

    # Time
    "time":        "time",
    "what time":   "time",
    "clock":       "time",

    # Date
    "date":        "date",
    "today":       "date",
    "what day":    "date",
    "day is it":   "date",

    # Jokes
    "joke":        "joke",
    "funny":       "joke",
    "laugh":       "joke",
    "humor":       "joke",
    "haha":        "joke",
    "lol":         "joke",
    "make me smile": "joke",

    # Motivation
    "motivat":     "motivation",
    "inspire":     "motivation",
    "quote":       "motivation",
    "encourage":   "motivation",

    # Python
    "python":      "python",
    "tip":         "python",
    "code":        "python",
    "programming": "python",
    "script":      "python",

    # Weather
    "weather":     "weather",
    "temperature": "weather",
    "rain":        "weather",
    "sunny":       "weather",

    # Thanks
    "thank":       "thanks",
    "thanks":      "thanks",
    "thx":         "thanks",
    "appreciate":  "thanks",

    # Farewell
    "bye":         "farewell",
    "goodbye":     "farewell",
    "exit":        "farewell",
    "quit":        "farewell",
    "see you":     "farewell",
    "later":       "farewell",
    "cya":         "farewell",
}


# ─────────────────────────────────────────────────────────────
#  CORE LOGIC
# ─────────────────────────────────────────────────────────────

def detect_category(user_input: str) -> str:
    """
    Identify the intent category from the user's message.

    Strategy:
    1. Lowercase the input.
    2. Check multi-word keywords first (longest match wins).
    3. Fall back to single-word keyword scan.
    4. Return 'fallback' if nothing matches.

    Parameters
    ----------
    user_input : str
        Raw text entered by the user.

    Returns
    -------
    str
        One of the category keys in RESPONSES.
    """
    text = user_input.lower().strip()

    # ── Sort keywords by length (longest first) for greedy match ──
    sorted_keywords = sorted(KEYWORDS.keys(), key=len, reverse=True)

    for keyword in sorted_keywords:
        if keyword in text:
            return KEYWORDS[keyword]

    return "fallback"


def get_response(category: str) -> str:
    """
    Pick a random reply from the appropriate RESPONSES category.
    Dynamic categories (time, date) are populated here.

    Parameters
    ----------
    category : str
        The detected intent category.

    Returns
    -------
    str
        The bot's reply text.
    """

    # ── Dynamic responses ────────────────────────────────────
    if category == "time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"⏰ The current time is {now}."

    if category == "date":
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"📅 Today is {today}."

    # ── Pick random reply from list ──────────────────────────
    options = RESPONSES.get(category, RESPONSES["fallback"])
    return random.choice(options)


def is_exit_command(user_input: str) -> bool:
    """Return True if the user typed an exit keyword."""
    exits = {"bye", "goodbye", "exit", "quit", "cya", "see you", "later"}
    text  = user_input.lower().strip()
    return any(word in text for word in exits)


# ─────────────────────────────────────────────────────────────
#  UI HELPERS
# ─────────────────────────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    print("=" * 55)
    print("       🤖  CODEBOT — Rule-Based Chatbot")
    print("        CodeAlpha Python Internship Project")
    print("=" * 55)
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 55)


def format_bot(message: str) -> str:
    """Prefix every bot line with the bot label."""
    lines = message.split("\n")
    formatted = []
    for i, line in enumerate(lines):
        if i == 0:
            formatted.append(f"\n  🤖 CodeBot : {line}")
        else:
            formatted.append(f"              {line}")
    return "\n".join(formatted)


# ─────────────────────────────────────────────────────────────
#  MAIN CHAT LOOP
# ─────────────────────────────────────────────────────────────

def chat():
    """Run the interactive chat session."""
    clear_screen()
    print_banner()

    # Greet the user on start
    print(format_bot(random.choice(RESPONSES["greetings"])))
    print()

    while True:
        # ── Get user input ───────────────────────────────────
        try:
            user_input = input("  👤 You       : ").strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl+C or piped input gracefully
            print(format_bot(random.choice(RESPONSES["farewell"])))
            break

        # ── Skip empty input ─────────────────────────────────
        if not user_input:
            print("  ⚠  Please type something!")
            continue

        # ── Check for exit ───────────────────────────────────
        if is_exit_command(user_input):
            print(format_bot(random.choice(RESPONSES["farewell"])))
            print()
            break

        # ── Detect category → get response → display ─────────
        category = detect_category(user_input)
        reply    = get_response(category)

        print(format_bot(reply))
        print()


# ── Run ──────────────────────────────────────────────────────
if __name__ == "__main__":
    chat()
