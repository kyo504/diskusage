# Diskusage program

## Purpose of this program
리눅스 환경에서, 입력받은 디스크의 사용량을 1 분마다 체크해서 90% 미만은 INFO, 95% 미만은 WARNING, 95% 이상은 ERROR 레벨의 로그를 기록하는 프로그램을 작성합니다.
ex) diskusage --mounted=/mnt/storage --logtype=file --logpath=/var/log/diskusage.log
--mount : 적절하지 못한 path 의 경우 에러로그 후 종료. default 는 /
--logtype : default stdout. 시간 남으면 file. 또 시간 남으면 syslog
--logpath : logtype 이 file 인 경우만 사용
(git clone 받아서 설치해서 사용해볼 수 있도록 만들어주시면 더 좋습니다. 유사한 다른 방법이어도 되고 패키지서버에 올려주셔도 됩니다.)

## Log format
level:INFO path:/mnt/storage capacity:5% size:8989800

## Program language to write the program
Python

## 구현에 필요한 사항
- 디스크에 정보를 시스템으로부터 얻어와야 한다.
- SetInterval로 주기적으로 callback을 호출해야 한다.

