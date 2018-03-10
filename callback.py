from bottle import default_app, route, request, abort
# from bottle import static_file
# from bottle import response
# from bottle import request, get, post
# from bottle import error, abort, redirect
# from bottle import template
from keybox import keybox


@route('/services')
@route('/services/')
def hello_world():
    return 'Hello from Bottle service! Update works, test #4'


def check_auth(req=None, abort_if_false=True):
    if req is None:
        req = request
    auth_valid = req.headers.get('Authorization') == keybox.master.token
    if not auth_valid and abort_if_false:
        abort(401, 'Invalid authorization')
    return auth_valid


bottle_app = default_app()
