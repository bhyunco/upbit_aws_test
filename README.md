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


---------------------------------------------------------

5) (추가)

selenium 구동방식

[패키지 리스트 업데이트]
sudo apt update

[pip3 설치]
sudo apt install python3-pip

[셀리니움 설치]
sudo pip install selenium


[chrome 설치]

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

sudo apt-get update

sudo apt-get install google-chrome-stable



[chrome 버전확인]

google-chrome --version



[chromedriver 버전 링크주소 복사하기]

(이 링크에 입장해서, 본인의 크롬버전에 맞게 복사해야함)

https://chromedriver.chromium.org/downloads

--> ex) https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip



[chromedriver 다운로드]

wget -N https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip



[chromedriver 압축해제]

(압축해제 기능 설치) sudo apt install unzip

(압축해제) unzip chromedriver_linux64.zip



[필요한 라이브러리 설치]

sudo pip install xlrd

sudo apt-get install xvfb

sudo pip install pyvirtualdisplay



[파이썬코드로 AWS UBUNTU에서 크롬창을 키는방법 - code 참조]


from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080))
display.start()

path='/home/ubuntu/chromedriver'
driver = webdriver.Chrome(path)
