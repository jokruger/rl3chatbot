# -*- coding: utf-8 -*-

import random
from src import app

reflections = {
    "i": "you",
    "am": "are",
    "i'm": "you are",
    "im": "you are",
    "was": "were",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

def reflect(token):
    t = token.lower()
    if t in reflections:
        return reflections[t]
    return token

def substitute(text, factsheet, apply_reflection):
    t = text
    for i in factsheet.get_facts():
        v = i.get_value()
        if apply_reflection:
            v = v.replace('!', ' ').replace('?', ' ').strip()
            v = ' '.join([reflect(j) for j in v.split(' ')])
        t = t.replace('{%s}' % i.get_label(), v)
    return t

def make_answer(templates, subfacts, background):
    t = random.choice(templates)
    t = substitute(t, subfacts, True)
    t = substitute(t, background, False)
    return t

@app.action('eliza_i_need')
def eliza_i_need(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Why do you need {g0}?",
        "Would it really help you to get {g0}?",
        "Are you sure you need {g0}?"
    ], subfacts, background))

@app.action('eliza_why_dont_you')
def eliza_why_dont_you(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Do you really think I don't {g0}?",
        "Perhaps eventually I will {g0}.",
        "Do you really want me to {g0}?"
    ], subfacts, background))

@app.action('eliza_why_cant_i')
def eliza_why_cant_i(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Do you think you should be able to {g0}?",
        "If you could {g0}, what would you do?",
        "I don't know - why can't you {g0}?",
        "Have you really tried?"
    ], subfacts, background))

@app.action('eliza_i_cant')
def eliza_i_cant(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "How do you know you can't {g0}?",
        "Perhaps you could {g0} if you tried.",
        "What would it take for you to {g0}?"
    ], subfacts, background))

@app.action('eliza_i_am')
def eliza_i_am(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Did you come to me because you are {g0}?",
        "How long have you been {g0}?",
        "How do you feel about being {g0}?"
        "How does being {g0} make you feel?",
        "Do you enjoy being {g0}?",
        "Why do you tell me you're {g0}?",
        "Why do you think you're {g0}?"
    ], subfacts, background))
