""" 
BSD 2-Clause License

Copyright (c) 2019,  Geoffrey J. Atkinson (geoffrey_atkinso@hotmail.com)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 
"""

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
    resp_json = json.dumps(resp.json)
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
