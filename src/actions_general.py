# -*- coding: utf-8 -*-

import random
from src import app

@app.action('')
def default(w, subfacts, conclusions, background, io):
    io.write('How can I help you?')

@app.action('goodbye')
def default(w, subfacts, conclusions, background, io):
    io.write(random.choice(["Thank you for talking with me.", "Good-bye.", "Thank you, that will be $150. Have a good day!"]))
    io.stop()
