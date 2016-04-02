# Diskusage program

# Contents

* [Description](#description)
* [Requirements](#requirements)
* [Options](#options)

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

ex) diskusage --mounted=/mnt/storage --logtype=file --logpath=/var/log/diskusage.log

----

지금까지는 프로그램에 대한 내용을 기술 한 것이고 아래는 어떻게 이 문제를 해결 했는지에 대한 내용을 기술한다

### 구현에 필요한 사항
- 디스크에 정보를 시스템으로부터 얻어와야 한다.
- SetInterval로 주기적으로 callback을 호출해야 한다.

