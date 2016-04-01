import logging
import logging.handlers

class Syslog
  log
  
  def __init__(self, name):
    log = logging.getLogger(__name__)
  
  def setLevel(self, level):
    
  def

log = logging.getLogger(__name__)

log.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')

formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
handler.setFormatter(formatter)

log.addHandler(handler)


def hello():
	log.debug('this is debug')
	log.critical('this is critical')

if __name__ == '__main__':
	hello()
