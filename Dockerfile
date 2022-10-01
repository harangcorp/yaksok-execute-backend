FROM python:3.9

RUN git clone http://github.com/yaksok/yaksok
WORKDIR /yaksok
RUN python setup.py install

EXPOSE 8080


RUN mkdir /app
COPY . /app
WORKDIR /app

RUN chown -R 1000:1000 /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "server.py"]