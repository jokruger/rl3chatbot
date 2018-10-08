# -*- coding: utf-8 -*-

from src import app

@app.action('')
def default(w, subfacts, conclusions, background, io):
    io.write('How can I help you?')

@app.action('hello')
def hello(w, subfacts, conclusions, background, io):
    io.write('Hi! Nice to meet you.')

@app.action('goodbye')
def goodbye(w, subfacts, conclusions, background, io):
    io.write('Bye-bye!')
    io.stop()
