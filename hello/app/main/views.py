
from . import main

@main.route('/index')
def index():
    return 'Hello, world!'
