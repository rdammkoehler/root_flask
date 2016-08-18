from injector import Injector

from n.s.f.app_module import APP
from .hello_world_app import HelloWorldModule

app = Injector(HelloWorldModule).get(APP)
