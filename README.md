# 디지털 북스 사용자

1) github 에 있는 파이썬 코드를 불러오기


[깃헙에서 코드 복사해오기]
git clone https://github.com/bhyunco/upbit_aws_test.git


---------------------------------------------------------
2) 사전 세팅

[패키지 리스트 업데이트]
sudo apt update

[pip3 설치]
sudo apt install python3-pip

[pandas 설치]
pip install pandas

[PyJWT 업그레이드]
pip install PyJWT --upgrade


---------------------------------------------------------
3) 구동 확인


[unt.py 실행]
python3 unt.py


---------------------------------------------------------
4) nohup을 이용한 background 서버 구동


[unt.py 코드 조회(보기,수정등)]
vim unt.py

[unt.py 를 background 에서 실행하기]
nohup python3 unt.py > ouplut.log &

[실행중인 프로그램 확인하기]
ps ax | grep .py

[background 프로그램 종료]
kill -9 PID
**(PID는 ps ax | grep .py를 했을때 확인 가능)
