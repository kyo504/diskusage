import argparse
import modules.Syslog as Syslog
import modules.timer as timer
import modules.Partition as Partition
import time
import math

@timer.setInterval(1, -1)
def startlogging(mylog, myPart):
	myPart.update();

	capa = myPart.getCapacity();
	used = myPart.getUsedSpace();
	loglevel = "INFO"

	if ( capa < 90 ):
		loglevel = "INFO"
	elif ( capa >=0 and capa < 95 ):
		loglevel = "WARNING"
	else:
		loglevel = "ERROR"

	mylog.write(loglevel, capa, used)

if __name__ == '__main__':

	# Parsing incoming arguements
	parser = argparse.ArgumentParser()
	parser.add_argument("--mounted", help="mount position")
	parser.add_argument("--logtype", help="log type : info, warning, error")
	parser.add_argument("--logpath", help="log path : stdout, file, syslof ")
	args = parser.parse_args()

	# If mount position is invalid, print error log and exit program

	mountpath = "/mnt/position"
	loglevel = "warning"

	mylog = Syslog.Syslog(mountpath, "stdout", "sample.log");
	myPart = Partition.Partition(args)

	stopper = startlogging(mylog, myPart)

	while 1:
		time.sleep(1)

	stopper.set()

