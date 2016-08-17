import multiprocessing
import os
import socket
import sys
from datetime import datetime

import pytz


class SimpleEvent(dict):
    def __init__(self, event='UNKNOWN', header={}, body=None):
        super(SimpleEvent, self).__init__()
        self['header'] = self.__default_header(event)
        self['header'].update(header)
        self['body'] = body

    def __default_header(self, event):
        default_header = {}
        default_header['version'] = '0.0.1'
        default_header['event'] = event
        default_header['time'] = datetime.utcnow().replace(tzinfo=pytz.utc).isoformat()
        default_header['host'] = {}
        default_header['host']['name'] = socket.gethostname()
        default_header['host']['IPv4'] = socket.gethostbyname(socket.gethostname())
        default_header['process'] = {}
        default_header['process']['name'] = multiprocessing.current_process().name
        default_header['process']['sys'] = {}
        default_header['process']['sys']['argv'] = sys.argv
        uname = os.uname()
        default_header['process']['sys']['uname'] = {}
        default_header['process']['sys']['uname']['sysname'] = uname.sysname
        default_header['process']['sys']['uname']['nodename'] = uname.nodename
        default_header['process']['sys']['uname']['release'] = uname.release
        default_header['process']['sys']['uname']['version'] = uname.version
        default_header['process']['sys']['uname']['machine'] = uname.machine
        times = os.times()
        default_header['process']['sys']['times'] = {}
        default_header['process']['sys']['times']['user'] = times.user
        default_header['process']['sys']['times']['system'] = times.system
        default_header['process']['sys']['times']['elapsed'] = times.elapsed
        default_header['process']['pid'] = os.getpid()
        default_header['process']['cwd'] = os.getcwd()
        loadavg = os.getloadavg()
        default_header['process']['load'] = {}
        default_header['process']['load'][1] = loadavg[0]
        default_header['process']['load'][5] = loadavg[1]
        default_header['process']['load'][15] = loadavg[2]
        default_header['encoding'] = 'utf-8'
        default_header['schema'] = 'UNKNOWN'
        return default_header

    @property
    def header(self):
        return self['header']

    @property
    def body(self):
        return self['body']
