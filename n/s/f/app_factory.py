from datetime import datetime

import pytz
from flask import Flask
from flask.ext.json import json_response

from .simple_event import SimpleEvent


class AppFactory:
    @staticmethod
    def build_app():
        app = Flask(__name__)
        app.config['JSON_ADD_STATUS'] = False
        app.config['JSON_STATUS_FIELD_NAME'] = 'status'

        @app.route('/info', methods=['GET'])
        def info():
            return json_response(status_=200, add_status_=True,
                                 info=SimpleEvent(event='INFO',
                                                  body={'check_time': datetime.now(tz=pytz.utc).isoformat()}))

        return app
