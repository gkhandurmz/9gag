FROM python:3


RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED 1

WORKDIR /9gag

ADD requirements.txt /9gag/

EXPOSE 5432

RUN pip install -r /9gag/requirements.txt

ADD . /9gag

