#!/usr/bin/env python3

import bot

chatbot = bot.DefaultChatbot()

print('Bot: Hello!\n')
user_input = ''
context = ''
while True:
    user_input = input('You: ')
    answer, context = chatbot.process(user_input, context)
    print('Bot: %s\n' % answer.message)
    if answer.stop:
        exit(0)
