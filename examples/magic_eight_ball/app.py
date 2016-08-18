from injector import Injector

from n.s.f.app_module import APP
from .eight_ball import EightBallModule

app = Injector(EightBallModule).get(APP)
