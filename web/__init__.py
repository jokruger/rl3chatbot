# -*- coding: utf-8 -*-

import json, uuid, logging, fcntl
from logging import Formatter, FileHandler
from datetime import timedelta
from flask import Flask, request, session, render_template, jsonify
from flask_compress import Compress
from werkzeug.contrib.fixers import ProxyFix
from bot import chatbot, chatbot_name

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('web.config')
Compress(app)

file_handler = FileHandler('chatbot.log')
file_handler.setLevel(logging.WARN)
file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(file_handler)

def log_message(ip, sid, msg):
    with open('dialogs', 'a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write('%s %s %s\n' % (str(ip), str(sid), msg))
        fcntl.flock(f, fcntl.LOCK_UN)

def init_sid(reset=False):
    sid = session.get('sid', None)
    if not sid or reset:
        sid = uuid.uuid1().hex
        session['sid'] = sid
    return sid

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=30)

@app.after_request
def after_request(response):
    return response

@app.route('/')
def view_index():
    sid = init_sid(reset=True)

    return render_template('page_index.html', debug_mode=app.config['DEBUG'], page='index', name=chatbot_name)

@app.route('/chat', methods=['POST'])
def view_chat():
    sid = init_sid()

    message = request.form.get('message', '')
    context = request.form.get('context', '')

    log_message(request.remote_addr, sid, 'USR: ' + message)

    try:
        answer, context = chatbot.process(message, context)
        if answer:
            message = answer.message
        else:
            message = 'ouch...'
    except Exception as e:
        message = 'ouch...'
        app.logger.exception(e)

    log_message(request.remote_addr, sid, 'BOT: ' + message)

    return jsonify(message=message, context=context)
