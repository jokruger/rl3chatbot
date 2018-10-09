# -*- coding: utf-8 -*-

import logging
from datetime import timedelta
from flask import Flask, request, session
from flask_compress import Compress
from logging import Formatter, FileHandler
from werkzeug.contrib.fixers import ProxyFix
from bot import chatbot

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('web.config')
Compress(app)

file_handler = FileHandler('chatbot.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(file_handler)

def ask_bot(question, context):
    context = {}
    response_text = 'hello'

    return response_text, context

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=30)

@app.after_request
def after_request(response):
    return response

from web import views
