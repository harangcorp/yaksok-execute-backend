FROM python:3.9

RUN git clone http://github.com/yaksok/yaksok
WORKDIR /yaksok
RUN python setup.py install

EXPOSE 8080


COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "server.py"]