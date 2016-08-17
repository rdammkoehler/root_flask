from injector import Injector

from n.s.f.app_module import APP, AppModule

app = Injector(AppModule).get(APP)
