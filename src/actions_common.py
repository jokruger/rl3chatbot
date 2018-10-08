# -*- coding: utf-8 -*-

from src import app

@app.action('')
def default(w, subfacts, conclusions, background, io):
    io.write('How can I help you?')
