
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
	2.  mounted path : `/`
	3.  log type: `stdout`
	4.  log path: `None`

	```Shell
	$ python3.4 main.py
	```
2. Run program with an argument which specifies invalid mounted position
	3. mounted path: `/not/existing/path`

	```Shell
	$ python3.4 main.py --mounted=/not/existing/path
	```

3. Run program with the given options
	4. mounted: `/valid/mounted/position`
	5. log type: `file`
	6. log path: `/your/desired/path/filename`

	```Shell
	$ python3.4 main.py --mounted=/valid/mount/path --logtype=file --logpath=/your/desired/path/diskusage.log
	```

4. Run program with the given options
	5. mounted path: `/valid/mounted/position`
	6. log type: `syslog`
	7. log path: `None`

	```Shell
	$ python3.4 main.py --mounted=/valid/mounted/position --logtype=syslog
	```

----

From now, I could describe the basic approach to implement this program and how I deal with some issues that I was faced with.

This program has 3 major features.

1. To parse incoming arguments vis command line
2. To retrieve disk information based on the given partition path
3. To write logs with pre-defined format
4. To set a timer to invoke callback periodically 

Basically, I tried to use modularization to simplify as much as possible in the main function. #1, #2, and #3 were implemented as class separately. And the last one(#4) is a module only containing function.

1, 2번에 대해서는 간단 하게 설명
3번에 대해서는 추가적인 설명이 필요하다...

