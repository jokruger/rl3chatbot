#!/usr/bin/env python3

from bot import chatbot

class MyIO():
    def __init__(self):
        pass

    def read(self):
        return input('You: ')

    def write(self, s):
        print('Bot: ' + s)
        print()

    def stop(self):
        exit(0)

print()

io = MyIO()
user_input = ''
while True:
    chatbot.process(user_input, io)
    user_input = io.read()
