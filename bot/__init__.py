# -*- coding: utf-8 -*-

import os, sys, random, rl3

class Answer():
    def __init__(self, message=None, stop=False):
        self.message = message
        self.stop = stop

class Chatbot():
    def __init__(self):
        self.actions = dict()

        self.intent_engine = rl3.RL3Engine()
        self.intent_engine.load('./intent.rl3c')

    def action(self, intent_name):
        def decorator(f):
            self.actions[intent_name] = f
            return f
        return decorator

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
            facts = self.intent_engine.create_factsheet_from_json(context) if context else self.intent_engine.create_factsheet()
            conclusions = self.intent_engine.create_factsheet()
            facts.retract_facts('text')
            facts.assert_simple_fact('text', user_input)
            self.intent_engine.run(facts, conclusions)
            for name, weight, subfacts in self.get_intents(conclusions):
                if name in self.actions:
                    answer = self.actions[name](weight, subfacts, conclusions, facts)
                    if answer:
                        facts.retract_facts('prior_intent')
                        facts.assert_simple_fact('prior_intent', name)
                        return (answer, facts.to_json())
        except:
            raise

        return (Answer(message='ouch...'), context)

chatbot_name = 'RL3ChatBot'
chatbot = Chatbot()

from bot import actions_general, actions_smalltalk
