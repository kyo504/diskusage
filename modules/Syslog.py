import logging
import logging.handlers

import os
import platform
import logging, logging.handlers
import sys
import syslog


'''
import syslog

syslog.syslog('Processing 11111')
syslog.syslog(syslog.LOG_ERR, 'Processing 22222')
syslog.syslog(syslog.LOG_ERR, 'E-mail processing initiated...')
'''

class Syslog:
	mountpath = ""
	logtype = ""
	loglevel = logging.WARNING
	logpath = ""
	logformat = 'level:%(level)7s path:%(path)s capacity:%(capacity)3d size:%(size)d'

	def __init__(self, mountpath, logtype, logpath):
		self.mountpath = mountpath
		self.logtype = logtype
		self.logpath = logpath

		self.logger = logging.getLogger("mylogger")
		self.setType(self.logtype)
		self.logger.setLevel(self.loglevel)

	def setType(self, logtype):
		# remove previous handler
		self.logger.handlers = [];

		if self.logtype == "file":
			logging.basicConfig(filename=self.logpath,level=self.loglevel, format=self.logformat)
			loghandler = logging.FileHandler(self.logpath)
		elif self.logtype == "syslog":
			logging.basicConfig(level=self.loglevel, format=self.logformat)
			# platform-dependent codes
			syslog_address = '/dev/log'
			if platform.system() == 'Darwin':
				syslog_address = '/var/run/syslog'
			loghandler = logging.handlers.SysLogHandler(address=syslog_address, facility=syslog.LOG_LOCAL1)
		else:
			logging.basicConfig(level=self.loglevel, format=self.logformat)
			loghandler = logging.StreamHandler(sys.stdout)
		
		# register the given handler to current logger
		self.logger.addHandler(loghandler)

	# log_level : INFO, WARNING, ERROR
	'''
	def setLevel(self, loglevel='info'):
		numeric_loglevel = getattr(logging, loglevel.upper(), None)
		if not isinstance(numeric_loglevel, int):
			raise ValueError('Invalid log level: "%s"\n Try: "debug", "info", "warning", "critical".' % loglevel)

		logging.basicConfig(level=numeric_loglevel, format='level:%(levelname)7s path:%(path)s capacity:%(capacity)3d size:%(size)d')

		# platform-dependent codes
		syslog_address = '/dev/log'
		if platform.system() == 'Darwin':
			syslog_address = '/var/run/syslog'

		log_handler = logging.handlers.SysLogHandler(address = syslog_address)
		self.logger.addHandler(log_handler)

		self.level = numeric_loglevel
	'''

	def write(self, level, capacity, size):
		# refer to the page for more deail information
		# https://docs.python.org/3/library/logging.html
		d = { 'level': level, 'path': self.mountpath, 'capacity': capacity, 'size': size }
		self.logger.warn("", extra=d)

