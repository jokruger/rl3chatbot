# -*- coding: utf-8 -*-

from src import app

@app.action('')
def default(w, fs, io):
    io.write('How can I help you?')

@app.action('hello')
def hello(w, fs, io):
    io.write('Hi! Nice to meet you.')

@app.action('goodbye')
def goodbye(w, fs, io):
    io.write('Bye-bye!')
    io.stop()
