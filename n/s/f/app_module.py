from injector import Key, Module, provides

from .app_factory import AppFactory

APP = Key('app')


class AppModule(Module):
    @provides(APP)
    def provide_app(self):
        return AppFactory.build_app()
