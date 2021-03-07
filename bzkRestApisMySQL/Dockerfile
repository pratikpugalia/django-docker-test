FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV LANG=C.UTF-8
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt-get update
RUN pip install -r requirements.txt
ADD . /code/