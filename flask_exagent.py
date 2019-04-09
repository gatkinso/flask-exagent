from flask import current_app, _app_ctx_stack, request
from google.protobuf.json_format import MessageToJson
import transport_pb2
import libagent as agent
import os, threading, datetime, uuid, json

def flask_exagent_before_req():
    current_trans = transport_pb2.Transport()
    current_trans.string_values["timestamp"] = str(datetime.datetime.utcnow())
    current_trans.string_values["uuid"] = str(uuid.uuid4())
    current_trans.string_values["pid"] = str(os.getpid())
    current_trans.string_values["tid"] = str(threading.get_ident())

    current_request = request._get_current_object()
    current_trans.string_values["base_url"] = current_request.base_url
    current_trans.string_values["endpoint"] = current_request.endpoint
    current_trans.string_values["method"] = current_request.method

    json_trans = MessageToJson(current_trans)

    agent.request(json_trans, "id")
    return None

def flask_exagent_after_req(resp):
    resp_json = r = json.dumps(resp.json)
    agent.response(resp_json, "id")
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

    def set_output_filename(self, filename):
        agent.set_config(filename)

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
