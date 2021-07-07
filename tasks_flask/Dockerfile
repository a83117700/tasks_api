FROM python:3.7.0-slim

WORKDIR /tasks_flask
ADD . /tasks_flask

RUN apt-get update && apt-get install -y gcc && apt-get install -y libc6-dev && apt-get install -y wget

RUN pip install --upgrade pip

RUN pip --no-cache-dir install -r requirements.txt

CMD ["uwsgi", "app.ini"]
