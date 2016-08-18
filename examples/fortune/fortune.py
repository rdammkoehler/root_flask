import os
import random

from flask.ext.json import json_response
from injector import Injector, Module, provides, inject, Key

from n.s.f.app_module import APP, AppModule

FORTUNE = Key('fortune')

FORTUNES = []


class Fortune:
    def __init__(self):
        self.file_name = 'fortunes'
        self.fortunes = self.load()

    def tell(self):
        return json_response(fortune=self.fortunes[random.randint(0, len(self.fortunes))])

    def load(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as fortune_file:
                return fortune_file.readlines()
        return []


class FortuneModule(Module):
    @provides(FORTUNE)
    @inject(app=APP, fortune=Fortune)
    def provide_fortune(self, app, fortune):
        app.add_url_rule('/fortune', 'fortune', fortune.tell)
        return app


if __name__ == '__main__':
    Injector([AppModule, FortuneModule]).get(FORTUNE).run()
