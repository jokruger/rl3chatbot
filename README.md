# rl3chatbot
A chatbot implemented with RL3 and Python.

The idea is to implement a small-talk bot logic as a core, and then build a specialized bot on top of it. Intent detection and NER are implemented in RL3. Answer generation logic is
implemented in Python 3, and is based on intents and entities detected during Intent/NER phase.

Core of the small-talk logic is based on Elize bot ideas.

Online demo https://chatbot.bdp.zorallabs.com

## Why RL3?

RL3 is like a regex on steroids. It provides both entity extraction and categorization features which makes it good fit for detecting intents in user input (i.e. categorize it) and
extract additional information from it (i.e. named entity recognition and parsing).

For more details on RL3 refer to https://rl3.zorallabs.com/wiki/Main_Page

## Dependencies

* RL3
* python 3
* flask
* flask-compress
