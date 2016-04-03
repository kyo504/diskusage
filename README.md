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

지금까지는 프로그램에 대한 내용을 기술 한 것이고 아래는 어떻게 이 문제를 해결 했는지에 대한 내용을 기술한다.

일단 이 프로그램에서의 주요 기능은 3가지다

1. CLI로 받은 argument를 파싱하는 작업
2. 주어진 파티션 위치에 대한 디스크 정보를 시스템으로 얻어오는 기능
3. 주기적으로 타이머 콜백이 동작하도록 해서 로그를 기록하도록 하는 기능

기본적으로 3가지 기능을 모듈로 묶어서 main에서의 로직은 최대한 간결하게 작성되도록 하였다. 1번과 2번에 대해서는 Class로 만들어서 객체를 생성한 이후에 이 객체를 통해서 모든 액션이 이루어지도록 했으며 3번의 경우에는 굳이 함수 하나만을 위해서 클래스를 만드는 것은 불필요해 보였기 때문에 함수로 유지하고 import만 하기로 했다.

====
1, 2번에 대해서는 간단 하게 설명
3번에 대해서는 추가적인 설명이 필요하다...

