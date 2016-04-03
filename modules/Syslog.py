import logging
import logging.handlers
import platform
import sys
import syslog

class Syslog:
	mountpath = ""
	logtype = ""
	loglevel = logging.WARNING
	logpath = ""
	logformat = 'level:%(level)7s path:%(path)s capacity:%(capacity)3d%% size:%(size)d'

	def __init__(self, mountpath, logtype, logpath):
		self.mountpath = mountpath
		self.logtype = logtype
		self.logpath = logpath

		self.logger = logging.getLogger("mylogger")
		self.logger.setLevel(self.loglevel)
		self.set_type(self.logtype)

	def set_type(self, logtype):
		# remove previous handler
		self.logger.handlers = [];

		if self.logtype == "file":
			logging.basicConfig(filename=self.logpath, level=self.loglevel, format=self.logformat)
			loghandler = logging.FileHandler(self.logpath)
		elif self.logtype == "syslog":
			#logging.basicConfig(level=self.loglevel, format=self.logformat)
			# platform-dependent codes
			syslog_address = '/dev/log'
			if platform.system() == 'Darwin':
				syslog_address = '/var/run/syslog'

			# Fixme :
			# loging to syslog does not work when calling basicConfig
			# For now, I apply alternative and and will see what the cause is
			loghandler = logging.handlers.SysLogHandler(address=syslog_address)
			loghandler.setFormatter(logging.Formatter(self.logformat))
		else:
			logging.basicConfig(level=self.loglevel, format=self.logformat)
			loghandler = logging.StreamHandler(sys.stdout)
		
		# register the given handler to current logger
		self.logger.addHandler(loghandler)

	def write(self, level, capacity, size):
		# refer to the page for more deail information
		# https://docs.python.org/3/library/logging.html
		d = { 'level': level, 'path': self.mountpath, 'capacity': capacity, 'size': size }
		self.logger.warning("", extra=d)

