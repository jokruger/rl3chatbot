# -*- coding: utf-8 -*-

import json, uuid
from flask import render_template, request, jsonify, session
from web import app, ask_bot
from bot import chatbot_name

def get_input(request, name):
    t = ''
    if name in request.form:
        t = request.form[name]
    return t

def init_uid():
    uid = session.get('uid', None)
    if not uid:
        try:
            uid = uuid.uuid1()
            session['uid'] = uid
        except:
            pass

    return uid

@app.route('/')
def view_index():
    uid = init_uid()

    return render_template('page_index.html', debug_mode=app.config['DEBUG'], page='index', name=chatbot_name)

@app.route('/chat', methods=['POST'])
def view_chat():
    uid = init_uid()

    message = get_input(request, 'message')
    context = get_input(request, 'context')

    app.logger.info('USER MESSAGE (%s): %s' % (str(uid), message))

    try:
        context = json.loads(context)
    except:
        context = {}

    try:
        message, context = ask_bot(message, context)
    except Exception as e:
        message = 'ouch...'
        app.logger.exception(e)

    return jsonify(message=message, context=context)
