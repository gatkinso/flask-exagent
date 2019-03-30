from flask import current_app, _app_ctx_stack

def flask_exagent_before_req():
    print("Before!")
    return None

def flask_exagent_after_req(res):
    print("After!")
    return resp

class FlaskExagent(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
            self.app.before_request(flask_exagent_before_req)
            self.app.after_request(flask_exagent_after_req)            

    def init_app(self, app):
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        ctx = _app_ctx_stack.top

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
