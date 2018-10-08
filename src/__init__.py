# -*- coding: utf-8 -*-

import os, sys, rl3

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
        name = ''
        weight = 0.0
        subfacts = None

        if fs.has_fact('intent'):
            for i in fs.get_facts('intent'):
                if i.get_weight() > weight:
                    name = i.get_value()
                    weight = i.get_weight()
                    if i.has_factsheet():
                        subfacts = i.get_factsheet()

        return (name, weight, subfacts)

    def process(self, user_input, io):
        conclusions = self.intent_engine.create_factsheet()
        self.facts.retract_facts('text')
        self.facts.assert_simple_fact('text', user_input)
        self.intent_engine.run(self.facts, conclusions)

        name, weight, subfacts = self.get_intent(conclusions)
        action = self.actions[name] if name in self.actions else self.actions['']

        action(weight, subfacts, conclusions, self.facts, io)

app = Chatbot()

from src import actions_basic
