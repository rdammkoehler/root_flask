import random

from flask.ext.json import json_response
from injector import Injector, Module, provides, inject

from n.s.f.app_module import APP, AppModule

PREMONITIONS = [
    'Yes.',
    'Yes, definitely.',
    'As I see it yes.',
    'It is certain.',
    'Without a doubt.',
    'It is decidedly so.',
    'You may rely on it.',
    'Outlook good.',
    'Most likely',
    'Signs point to yes.',
    'My reply is no.',
    'My sources say no.',
    'Very doubtful.',
    'Outlook not so good.',
    'Dont count on it.',
    'Cannot predict now',
    'Ask again later.',
    'Better not tell you now.',
    'Cannot predict now.',
    'Reply hazy. Try again.',
    'Concentrate and ask again.',
]


class Eightball:
    def foresee(self):
        return json_response(prediction=self.select())

    def select(self):
        return PREMONITIONS[random.randint(0, len(PREMONITIONS))]


class EightBallModule(Module):
    @provides(APP)
    @inject(eightball=Eightball)
    def provide_app(self, eightball):
        app = Injector(AppModule).get(APP)
        app.add_url_rule('/foresee', 'foresee', eightball.foresee)
        return app


if __name__ == '__main__':
    Injector(EightBallModule).get(APP).run()
