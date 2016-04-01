import os
import platform
import logging, logging.handlers

def setLogLevel(loglevel='debug'):
    numeric_loglevel = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_loglevel, int):
        raise ValueError('Invalid log level: "%s"\n Try: "debug", "info", "warning", "critical".' % loglevel)

    logging.basicConfig(level=numeric_loglevel, format='%(asctime)s %(name)s %(levelname)s %(message)s')

    program = os.path.basename(__file__)
    logger = logging.getLogger(program)
    
    syslog_address = '/dev/log'
    if platform.system() == 'Darwin':
        syslog_address = '/var/run/syslog'

    print(syslog_address)
        
    log_handler = logging.handlers.SysLogHandler(address = syslog_address)
    logger.addHandler(log_handler)

    return logger

logger = setLogLevel()
logger.info('Hello Log')