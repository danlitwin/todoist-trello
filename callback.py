
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route
#from bottle import static_file
#from bottle import response
#from bottle import request, get, post
#from bottle import error, abort, redirect
#from bottle import template


@route('/services')
def hello_world():
    return 'Hello from Bottle!'

application = default_app()


