class Hello(object):
  def __init__(self, name):
    self.name = name

  def __call__(self, environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello, World! by %s' % (self.name)]

def create_hello(global_config, **local_conf):
  return Hello(local_conf['author_name'])
