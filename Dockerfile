FROM python:3.7-slim

ENV PYTHONDOWNTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /BookstoreDemo

COPY Pipfile Pipfile.lock /BookstoreDemo/
RUN pip install pipenv && pipenv install --system

COPY . /BookstoreDemo/