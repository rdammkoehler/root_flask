from injector import Injector

from n.s.f.app_module import AppModule
from .fortune import FortuneModule, FORTUNE

app = Injector([AppModule, FortuneModule]).get(FORTUNE)
