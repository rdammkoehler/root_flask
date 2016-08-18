from injector import Injector

from n.s.f.app_module import APP
from .fortune import FortuneModule

app = Injector(FortuneModule).get(APP)
