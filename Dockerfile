FROM python:3.9

RUN git clone http://github.com/yaksok/yaksok
WORKDIR /yaksok
RUN python setup.py install

EXPOSE 8080

RUN pip3 install -r requirements.txt


COPY . /app
WORKDIR /app

ENTRYPOINT ["python", "server.py"]