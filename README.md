
# Diskusage program

> I've tested this program on OS X, Ubuntu 12.04LTS(32bit)

# Contents

* [Description](#description)
* [Requirements](#requirements)
* [Options](#options)
* [Test cases](#testcases)

### <a name="description"></a>Description
This program periodically writes a log message onto the given disk and the log message has a pre-defined format.

### <a name="requirements"></a>Requirements

- Program should run on linux environment
- Usage of disk is checked in every 1 minute
- Depending on the ratio, the level of log is different
	- 0% ~ 89% : INFO
	- 90% ~ 94% :  WARNING
	- 95% ~ : ERROR
- program is written in Python
- The log format is like below
	- `level:INFO path:/mnt/storage capacity:5% size:8989800`

### <a name="options"></a>Options

There are three arguments and the description of each is described below: 

 - mounted: for the invalid mounted path, the program prints error log and exit. Default path is `/`
 - logtype: `stdout`, `file`, `syslog`
 - logpath: This is optional argument and only used in case that logotype is `file`

### <a name="testcases"</a>Test Cases

1. Run program with default values
	2. Options : default(mounted path= `/`, log type= `stdout`, log path= `None`)
	3. Command	
	```Shell
	$ python3.4 main.py
	```
	4. Expected result: log data displays via stdout
	
2. Run program with an argument which specifies invalid mounted position
	3. Options: mounted path= `/not/existing/path`
	4. Command
	```Shell
	$ python3.4 main.py --mounted=/not/existing/path
	```
	4. Expected Result: Program is terminated with error message


3. Run program with the given options
	4. Options: mounted= `/valid/mounted/position`,	log type= `file`, log path=`/your/desired/path/filename`
	5. Command
	```Shell
	$ python3.4 main.py --mounted=/valid/mount/path --logtype=file --logpath=/your/desired/path/diskusage.log
	```
	6. Expected Result: Log data is stored in the specified path as text file


4. Run program with the given options
	5. Options: mounted path= `/valid/mounted/position`, log type= `syslog`, log path= `None`
	6. Command
	```Shell
	$ python3.4 main.py --mounted=/valid/mounted/position --logtype=syslog
	```
	7. Expected Result: Log data is stored as system log.

----

From now, I could describe the basic approach to implement this program and how I deal with some issues that I was faced with.

This program has 3 major features.

1. To parse incoming arguments vis command line
2. To retrieve disk information based on the given partition path
3. To write logs with pre-defined format
4. To set a timer to invoke callback periodically 

Basically, I tried to use modularization to simplify as much as possible in the main function. #1, #2, and #3 were implemented as class separately. And the last one(#4) is a module only containing function.
