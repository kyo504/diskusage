import logging
import logging.handlers

my_logger = logging.getLogger('MyLogger')

my_logger.setLevel(logging.WARNING)

#logging.basicConfig(level=logging.WARNING, format='level:%(level)7s path:%(path)s capacity:%(capacity)3d%% size:%(size)d')
#logging.basicConfig(level=logging.WARNING)
handler = logging.handlers.SysLogHandler(address='/var/run/syslog')
handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)s:%(filename)s:%(lineno)d -- %(message)s'))
my_logger.addHandler(handler)

'''
my_logger.warn('waring 111')
my_logger.critical('critical 222')
'''


d = { 'level': "INFO", 'path': '/', 'capacity': 80, 'size': 101010 }
my_logger.warn('1111111', extra=d)
my_logger.critical('2222222 ', extra=d)
