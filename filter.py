class Filter1(object):
  def __init__(self, app, name):
    self.app = app
    self.name = name

  def __call__(self, environ, start_response):
    print('filter: %s' % (self.name)) 
    return self.app(environ, start_response)

def filter1_factory(global_config, **local_conf):
  def _filter(app):
    return Filter1(app, local_conf['filter_name'])
  return _filter
