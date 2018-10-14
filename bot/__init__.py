# -*- coding: utf-8 -*-

import os, sys, random, rl3
from bot.core import Option, Answer
from bot.base import BaseActions
from bot.wikipedia import WikipediaActions
from bot.smalltalk import SmallTalkActions

class Chatbot():
    def __init__(self, name, model_path):
        self.name = name
        self.engine = rl3.RL3Engine()
        self.engine.load(model_path)

    def get_name(self):
        return self.name

    def get_intents(self, fs):
        groups = dict()
        for i in fs.get_facts('intent'):
            k = int(i.get_weight() * 1000)
            if k not in groups:
                groups[k] = []
            groups[k].append((i.get_value(), i.get_weight(), i.get_factsheet() if i.has_factsheet() else None))
        intents = []
        for i in sorted(groups.keys(), reverse=True):
            t = groups[i]
            random.shuffle(t)
            intents += t
        return intents

    def process(self, user_input, context):
        try:
            facts = self.engine.create_factsheet_from_json(context) if context else self.engine.create_factsheet()

            # reset 'bot name' fact
            facts.retract_facts('bot_name')
            facts.assert_simple_fact('bot_name', self.get_name())

            # reset 'user input' fact
            facts.retract_facts('text')
            facts.assert_simple_fact('text', user_input)

            conclusions = self.engine.create_factsheet()
            self.engine.run(facts, conclusions)
            for name, weight, subfacts in self.get_intents(conclusions):
                action = getattr(self, name, None)
                if action is not None:
                    answer = action(weight, subfacts, conclusions, facts)
                    if answer:
                        facts.retract_facts('prior_intent')
                        facts.assert_simple_fact('prior_intent', name)
                        return (answer, facts.to_json())
        except:
            raise

        return (Answer(message='ouch...'), context)

class DefaultChatbot(Chatbot, BaseActions, WikipediaActions, SmallTalkActions):
    def __init__(self):
        Chatbot.__init__(self, 'RL3Bot', './intent.rl3c')
        BaseActions.__init__(self)
        WikipediaActions.__init__(self)
        SmallTalkActions.__init__(self)
