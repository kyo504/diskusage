import argparse

class ArgInfo:

	# Private member variables
	_mountedpath = '/'
	_logtype = 'stdout'
	_logpath = ''

	def __init__(self):
		# Parsing incoming arguements
		parser = argparse.ArgumentParser()
		parser.add_argument("--mounted", help="mounted position")
		parser.add_argument("--logtype", help="stdout, file, syslog")
		parser.add_argument("--logpath", help="file path which stores log data")
		args = parser.parse_args()

		if args.mounted:
			self._mountedpath = args.mounted 

		if args.logtype:
			self._logtype = args.logtype

		if args.logpath:
			self._logpath = args.logpath

	@property
	def mountedpath(self):
		return self._mountedpath

	@property
	def logtype(self):
		return self._logtype
	
	@property
	def logpath(self):
		return self._logpath
	



