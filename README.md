
# Diskusage program


# Contents

* [Description](#description)
* [Requirements](#requirements)
* [Options](#options)
* [Test Cases](#testcases)
* [Development Log](#devlog)

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

> Test Environment
> Platform : OS X, Ubuntu 12.04LTS(32bit)
> Language : Python 3.4


1. Run program with default values
	- Options : default(mounted path= `/`, log type= `stdout`, log path= `None`)
	- Command	
	```Shell
	$ python3.4 main.py
	```
	- Expected result: log data displays via stdout
	
2. Run program with an argument which specifies invalid mounted position
	- Options: mounted path= `/not/existing/path`
	- Command
	```Shell
	$ python3.4 main.py --mounted=/not/existing/path
	```
	- Expected Result: Program is terminated with error message


3. Run program with the given options
	- Options: mounted= `/valid/mounted/position`,	log type= `file`, log path=`/your/desired/path/filename`
	- Command
	```Shell
	$ python3.4 main.py --mounted=/valid/mount/path --logtype=file --logpath=/your/desired/path/diskusage.log
	```
	- Expected Result: Log data is stored in the specified path as text file


4. Run program with the given options
	- Options: mounted path= `/valid/mounted/position`, log type= `syslog`, log path= `None`
	- Command
	```Shell
	$ python3.4 main.py --mounted=/valid/mounted/position --logtype=syslog
	```
	- Expected Result: Log data is stored as system log.

### <a name="devlog"</a>Development Log

From now, I could describe the basic approach to implement this program and how I deal with some issues that I was faced with.

This program has 4 major features.

1. To parse incoming arguments vis command line
2. To retrieve disk or partition information based on the given mounted path
3. To write logs with pre-defined format
4. To set a timer to invoke callback periodically 

Basically, I use modularization to simplify the main function as much as possible. Therefore #1, #2, and #3 are implemented as class separately, and the last one(#4) is a module only containing function.

During designing overall program structure, **timer** was the most difficult part. From my previous experience, I thought *SetInterval* in javasciprt is the best fit to achieve the goal but there was a nice and neat way in python. Therefore I googled and found some possible solutions.

- Using *threading*
- Using *sched*
- Using *Advanced python scheduler*

Among those solutions above, I choose the first one because I am a bit more familiar than others. There are two ways to implement **SetInterval**.

1. Decorator function with decorator arguments
2. Standalone function without decorator

Even though I implemented two functions, the fundamental concept of the two is the same. 

- Call timer function with an interval value. ]
- Create a thread and run start-routine
- Wait for the given interval and if flag is not set run another loop
- Stop loop if the flag is set to `true` by calling `set` function
