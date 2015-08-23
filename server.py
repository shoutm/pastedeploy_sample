#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from paste.deploy import loadapp
from wsgiref.simple_server import make_server

if __name__ == '__main__':
  path = os.path.dirname(__file__)
  wsgi_app = loadapp('config:paste.cfg', relative_to=path)
  httpd = make_server('', 8080, wsgi_app)
  httpd.serve_forever()
