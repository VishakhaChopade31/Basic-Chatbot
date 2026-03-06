# 🤖 Basic Rule-Based Chatbot (CodeBot)

**CodeAlpha Python Programming Internship — Project 3**

---

## 📌 Project Overview

**CodeBot** is a friendly, interactive rule-based chatbot built entirely in
Python — no AI/ML libraries required. It scans the user's input for keywords,
maps them to response categories, and replies with one of several pre-written
messages chosen at random. This gives the bot a natural, varied feel despite
its simple logic.

---

## ✨ Features

| Capability | Keywords That Trigger It |
|---|---|
| Greetings | hello, hi, hey, howdy, good morning… |
| Status check | how are you, how r u, feeling, doing |
| Bot identity | name, who are you, what are you |
| Help menu | help, commands, options, topics |
| Current time | time, what time, clock |
| Current date | date, today, what day |
| Tell a joke | joke, funny, laugh, lol |
| Motivational quote | motivate, inspire, quote, encourage |
| Python tips | python, tip, code, programming |
| Weather info | weather, temperature, rain |
| Gratitude | thank, thanks, thx, appreciate |
| Goodbye | bye, exit, quit, goodbye, cya |

---

## 🧠 Python Concepts Used

- **Dictionaries** — keyword mapping and response library
- **Lists** — multiple replies per category
- **Functions** — `detect_category()`, `get_response()`, `chat()`
- **`random` module** — `random.choice()` for varied replies
- **`datetime` module** — live time and date responses
- **String methods** — `.lower()`, `.strip()`, `in` operator
- **`if-elif-else`** — category routing logic
- **`while` loop** — keeps the chat running until exit
- **`try/except`** — graceful handling of Ctrl+C

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed ([python.org](https://www.python.org/downloads/))

### Steps

```bash
# 1. Navigate to the project folder
cd Basic_Chatbot

# 2. Run the chatbot
python chatbot.py
```

> ✅ No external libraries required — uses Python standard library only.

---

## 💬 Example Conversation

```
🤖 CodeBot : Hey there! 😊 How can I help you today?

👤 You       : hello
🤖 CodeBot : Hi! I'm CodeBot — your friendly Python assistant. What's up?

👤 You       : tell me a joke
🤖 CodeBot : Why do programmers prefer dark mode?
              Because light attracts bugs! 🐛😄

👤 You       : what time is it
🤖 CodeBot : ⏰ The current time is 03:45 PM.

👤 You       : python tip
🤖 CodeBot : 🐍 Python Tip: Use f-strings for fast, readable formatting!
              name = "World"; print(f"Hello, {name}!")

👤 You       : bye
🤖 CodeBot : Goodbye! Have a wonderful day! 👋
```

---

## ⚙️ How It Works

```
User Input
    ↓
detect_category()  — scans input for known keywords
    ↓
get_response()     — picks a random reply from the category
    ↓
format_bot()       — formats the output with the bot prefix
    ↓
Printed to Console
```

---

## 📁 File Structure

```
Basic_Chatbot/
├── chatbot.py    ← Main program
└── README.md     ← This file
```

---

## 👤 Author

**CodeAlpha Python Internship**
www.codealpha.tech
