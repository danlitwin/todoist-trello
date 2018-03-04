from bottle import default_app, route
#from bottle import static_file
#from bottle import response
#from bottle import request, get, post
#from bottle import error, abort, redirect
#from bottle import template

@route('/services')
@route('/services/')
def hello_world():
    return 'Hello from Bottle service! Update works, test #4'

bottle_app = default_app()
