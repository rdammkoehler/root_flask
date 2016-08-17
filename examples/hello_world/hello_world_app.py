from flask.ext.json import json_response
from injector import Injector, Module, provides

from n.s.f.app_module import APP, AppModule


class HelloAppFactory:
    @staticmethod
    def decorate_app(app):
        @app.route('/hello', methods=['GET'])
        def hello():
            return json_response(message='hello world')

        return app


class HelloWorldModule(Module):
    @provides(APP)
    def provide_app(self):
        return HelloAppFactory.decorate_app(Injector(AppModule).get(APP))


if __name__ == '__main__':
    app = Injector(HelloWorldModule).get(APP)
    app.run()
