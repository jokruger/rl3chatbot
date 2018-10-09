#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from web import app

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'http'
    app.run(host='0.0.0.0', port=8400)
