# rl3chatbot
A simple chatbot implemented with Python and RL3.

The idea is to implement a well-known Elize bot logic as a core, and then build a specialized bot on top of it. Intent detection and NER will be implemented in RL3. Answer generation logic will be
implemented in Python 3, and will be based on intents and entities detected.

## Why RL3?

RL3 is like a regex on steroids. It provides both entity extraction and categorization features which makes it good fit for detecting intents in user input (i.e. categorize it) and
extract additional information from from it (i.e. named entity recognition and parsing).

For more details on RL3 refer to https://rl3.zorallabs.com/wiki/Main_Page
