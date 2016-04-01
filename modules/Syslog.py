import logging
import logging.handlers

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
        
    log_handler = logging.handlers.SysLogHandler(address = syslog_address)
    logger.addHandler(log_handler)

    return logger


class Syslog:
	def __init__(self):
		self.logger = logging.getLogger()
		# In case of OSX, address should be 
		#handler = logging.handlers.SysLogHandler(address='/var/run/syslog')
		#formatter = logging.Formatter('%(module)s.%(funcName)s: %(message)s')
		#self.log.addHandler(handler)

	# log_level : INFO, WARNING, ERROR
	def setLevel(self, loglevel='info'):
		numeric_loglevel = getattr(logging, loglevel.upper(), None)
		if not isinstance(numeric_loglevel, int):
			raise ValueError('Invalid log level: "%s"\n Try: "debug", "info", "warning", "critical".' % loglevel)

		logging.basicConfig(level=numeric_loglevel, format='%(asctime)s %(name)s %(levelname)s %(message)s')

		syslog_address = '/dev/log'
		if platform.system() == 'Darwin':
			syslog_address = '/var/run/syslog'

		log_handler = logging.handlers.SysLogHandler(address = syslog_address)
		self.logger.addHandler(log_handler)

		self.level = loglevel



	def write(self, msg):
		numeric_loglevel = getattr(logging, self.level.upper(), None)
		print(numeric_loglevel)
		if not isinstance(numeric_loglevel, int):
			raise ValueError('Invalid log level: "%s"\n Try: "debug", "info", "warning", "critical".' % loglevel)

		if self.level == logging.WARNING:
			print("WARNING")
			self.logger.warning(msg)
		elif self.level == logging.ERROR:
			print("ERROR")
			self.logger.error(msg)
		else:
			print("INFO")
			self.logger.info(msg)
