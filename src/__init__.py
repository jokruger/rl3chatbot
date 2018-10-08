# -*- coding: utf-8 -*-

import os, sys, random, rl3

class Chatbot():
    def __init__(self):
        self.actions = dict()

        self.intent_engine = rl3.RL3Engine()
        self.intent_engine.load('./intent.rl3c')

        self.facts = self.intent_engine.create_factsheet()

    def action(self, intent_name):
        def decorator(f):
            self.actions[intent_name] = f
            return f
        return decorator

    def get_intent(self, fs):
        intents = []
        if fs.has_fact('intent'):
            weight = 0.0
            for i in fs.get_facts('intent'):
                if i.get_weight() > weight:
                    weight = i.get_weight()
            for i in fs.get_facts('intent'):
                if abs(weight - i.get_weight()) < 0.0001 :
                    n = i.get_value()
                    w = i.get_weight()
                    s = None
                    if i.has_factsheet():
                        s = i.get_factsheet()
                    t = (n, w, s)
                    intents.append(t)

        if len(intents) > 0:
            return random.choice(intents)

        return ('', 0.0, None)

    def process(self, user_input, io):
        conclusions = self.intent_engine.create_factsheet()
        self.facts.retract_facts('text')
        self.facts.assert_simple_fact('text', user_input)
        self.intent_engine.run(self.facts, conclusions)

        name, weight, subfacts = self.get_intent(conclusions)
        action = self.actions[name] if name in self.actions else self.actions['']

        action(weight, subfacts, conclusions, self.facts, io)

app = Chatbot()

from src import actions_common, actions_eliza
