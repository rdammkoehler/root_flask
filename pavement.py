import os

from paver.easy import *
from paver.setuputils import setup, find_packages

setup(
    name='root-flask',
    packages=find_packages(exclude=['test', 'test.*']),
    include_package_data=True,
    version='0.0.1.dev',
    install_requires=[
        'flask',
        'gunicorn',
        'Flask-JSON',
        'python-dateutil',
        'injector',
    ],
    entry_points={
    })


@task
def autopep8():
    sh("autopep8 --in-place --recursive .")


@task
def flake8():
    sh("flake8 n")


@task
@needs(['environment'])
def test():
    sh("nosetests --with-xunit --with-cover --cover-package n --cover-inclusive --cover-erase --cover-branches",
       env=_make_env())
    sh('python3 -m coverage xml --omit "n/__init__.py"')
    sh('python3 -m coverage report --fail-under=90')


@task
@needs(['flake8', 'test', 'bdist_wheel'])
def default():
    pass


@task
@needs(['environment'])
def behave():
    sh("behave", env=_make_env())


@task
def itest():
    env = _make_env()
    sh("nosetests itest", env=env)


@task
@needs(['default', 'behave', 'itest'])
def ci():
    pass


@task
@cmdopts([('env=', 'e', 'environment to use')])
def environment():
    pass


@task
@needs(['environment'])
def gunicorn():
    sh("gunicorn n.s.f.example:app", env=_make_env())


def _make_env():
    nsf_env = options.get('env', 'local')
    env = os.environ.copy()
    env['NSF_ENV'] = nsf_env
    return env
