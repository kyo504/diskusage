import modules.Syslog as Syslog
import argparse





if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--mounted", help="mount position")
	parser.add_argument("--logtype", help="log type : info, warning, error")
	parser.add_argument("--logpath", help="log path : stdout, file, syslof ")

	args = parser.parse_args()
	print(args.mounted)
	print(args.logtype)
	print(args.logpath)

	# If mount position is invalid, print error log and exit program





	mylog = Syslog.Syslog()


	mylog.setLevel("warning")
	mylog.write("This is WARNING level log")

	mylog.setLevel("error")
	mylog.write("This is ERROR level log")

	mylog.setLevel("info")
	mylog.write("This is INFO level log")

