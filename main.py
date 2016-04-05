import time
import sys

#User-defined modules
from modules.syslog import Syslog 
from modules.partition import PartitionInfo
from modules.arginfo import ArgInfo
import modules.timer as timer

# Timer callback will be invoked in every 1 minute
@timer.set_interval(1)
def start_logging(mylog, myPart):
	myPart.update();

	capa = myPart.get_capacity();
	used = myPart.get_used_space();

	if ( capa < 90 ):
		loglevel = "INFO"
	elif ( capa >=0 and capa < 95 ):
		loglevel = "WARNING"
	else:
		loglevel = "ERROR"

	mylog.write(loglevel, capa, used)

if __name__ == '__main__':

	# Create an object which contains incoming arguments information
	args = ArgInfo()

	# If mount position is invalid, print error log and exit program
	if PartitionInfo.is_mounted(args.mountedpath) == False:
		print("The given path({0:s}) is not mounted, so program is intentionally terminated".format(args.mountedpath))
		sys.exit()

	partInfo = PartitionInfo(args.mountedpath)
	logInfo = Syslog(args.mountedpath, args.logtype, args.logpath);

	print(">>>> Start logging <<<<")
	stop = start_logging(logInfo, partInfo)
	#cancel_calls = start_logging(logInfo, partInfo)

	while 1:
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			print("Proram is terminated by KeyboardInterrupt")
			sys.exit();

	stop.set() # Stop timer
	#cancel_calls()
	print(">>>> End logging <<<<")

