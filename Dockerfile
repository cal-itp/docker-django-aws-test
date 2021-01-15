FROM python:3.8
ENV PYTHONUNBUFFERED 1

EXPOSE 8080

WORKDIR /usr/src/django

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY manage.py manage.py
COPY app/ app/