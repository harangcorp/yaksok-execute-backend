FROM python:3.9

RUN git clone http://github.com/yaksok/yaksok
WORKDIR /yaksok
RUN python setup.py install


COPY . /app

WORKDIR /app

# 필요한 의존성 file들 설치
RUN pip3 install -r requirements.txt

# container가 구동되면 실행
ENTRYPOINT ["python", "server.py"]