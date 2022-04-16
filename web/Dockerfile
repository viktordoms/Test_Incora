FROM python:3.9.5-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /Test_Incora

WORKDIR /Test_Incora

COPY ./requirements.txt /Test_Incora


RUN  pip install --upgrade pip && pip install -r requirements.txt

CMD ./wait-for-it.sh db:5432 -- python3 ./Test_Incora/manage.py runserver 0.0.0.0:8010