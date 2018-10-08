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
    if factsheet is not None and len(factsheet) > 0:
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

@app.action('eliza_are_you')
def eliza_are_you(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Why does it matter whether I am {g0}?",
        "Would you prefer it if I were not {g0}?",
        "Perhaps you believe I am {g0}.",
        "I may be {g0} - what do you think?"
    ], subfacts, background))


@app.action('eliza_base_question')
def eliza_base_question(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Why do you ask?",
        "How would an answer to that help you?",
        "What do you think?"
        "How do you suppose?",
        "Perhaps you can answer your own question.",
        "What is it you're really asking?"
    ], subfacts, background))

@app.action('eliza_because')
def eliza_because(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Is that the real reason?",
        "What other reasons come to mind?",
        "Does that reason apply to anything else?",
        "If {g0}, what else must be true?"
    ], subfacts, background))

@app.action('eliza_sorry')
def eliza_sorry(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "There are many times when no apology is needed.",
        "What feelings do you have when you apologize?"
    ], subfacts, background))


@app.action('eliza_hello')
def eliza_hello(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Hello... I'm glad you could drop by today.",
        "Hi there... how are you today?",
        "Hello, how are you feeling today?"
    ], subfacts, background))

@app.action('eliza_i_think')
def eliza_i_think(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Do you doubt {g0}?",
        "Do you really think so?",
        "But you're not sure {g0}?"
    ], subfacts, background))

@app.action('eliza_friend')
def eliza_friend(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Tell me more about your friends.",
        "When you think of a friend, what comes to mind?",
        "Why don't you tell me about a childhood friend?"
    ], subfacts, background))

@app.action('eliza_yes')
def eliza_yes(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "You seem quite sure.",
        "OK, but can you elaborate a bit?"
    ], subfacts, background))

@app.action('eliza_computer')
def eliza_computer(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Are you really talking about me?",
        "Does it seem strange to talk to a computer?",
        "How do computers make you feel?",
        "Do you feel threatened by computers?"
    ], subfacts, background))

@app.action('eliza_is_it')
def eliza_is_it(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Do you think it is {g0}?",
        "Perhaps it's {g0} - what do you think?",
        "If it were {g0}, what would you do?",
        "It could well be that {g0}."
    ], subfacts, background))

@app.action('eliza_it_is')
def eliza_it_is(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "You seem very certain.",
        "If I told you that it probably isn't {g0}, what would you feel?"
    ], subfacts, background))

@app.action('eliza_can_you')
def eliza_can_you(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "What makes you think I can't {g0}?",
        "If I could {g0}, then what?",
        "Why do you ask if I can {g0}?"
    ], subfacts, background))

@app.action('eliza_can_i')
def eliza_can_i(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Perhaps you don't want to {g0}.",
        "Do you want to be able to {g0}?",
        "If you could {g0}, would you?"
    ], subfacts, background))

@app.action('eliza_you_are')
def eliza_you_are(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Why do you think I am {g0}?",
        "Does it please you to think that I'm {g0}?",
        "Perhaps you would like me to be {g0}.",
        "Perhaps you're really talking about yourself?"
        "Why do you say I am {g0}?",
        "Why do you think I am {g0}?",
        "Are we talking about you, or me?"
    ], subfacts, background))

@app.action('eliza_i_dont')
def eliza_i_dont(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Don't you really {g0}?",
        "Why don't you {g0}?",
        "Do you want to {g0}?"
    ], subfacts, background))

@app.action('eliza_i_feel')
def eliza_i_feel(w, subfacts, conclusions, background, io):
    io.write(make_answer([
        "Good, tell me more about these feelings.",
        "Do you often feel {g0}?",
        "When do you usually feel {g0}?",
        "When you feel {g0}, what do you do?"
    ], subfacts, background))
