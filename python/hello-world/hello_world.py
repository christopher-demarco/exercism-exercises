def hello(name=''):
    if name in ('', None): name = 'World'
    return "Hello, %s!" % name
