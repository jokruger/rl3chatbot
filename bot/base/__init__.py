# -*- coding: utf-8 -*-

import random, re
from bot.answer import Answer

def substitute(text, factsheet):
    t = text
    if factsheet is not None and len(factsheet) > 0:
        for i in factsheet.get_facts():
            t = t.replace('{%s}' % i.get_label(), i.get_value())
    return t

def make_answer(templates, context):
    random.shuffle(templates)
    for i in templates:
        try:
            t = substitute(i, context)
            if re.search(r"{[a-zA-Z0-9_\-]+}", t) is None:
                return Answer(message=t)
        except:
            pass

    return None

class BaseActions():
    def __init__(self):
        pass

    def goodbye(self, w, subfacts, conclusions, context):
        return Answer(message=random.choice([
            "Thank you for talking with me.",
            "Good-bye.",
            "Thank you, that will be $150. Have a good day!"
        ]), stop=True)

    def bot_name(self, w, subfacts, conclusions, context):
        return Answer(message="Yes?")

    def what_is_your_name(self, w, subfacts, conclusions, context):
        return make_answer([
            "You can call me {bot_name}.",
            "Call me {bot_name}.",
            "My name is {bot_name}.",
        ], context)

    def who_are_you(self, w, subfacts, conclusions, context):
        return make_answer(["I am {bot_name} - a computer program designed to simulate conversation with human users."], context)
