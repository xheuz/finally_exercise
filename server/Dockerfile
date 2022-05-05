FROM python:3.10-alpine

# Remove buffer from docker
ENV PYTHONUNBUFFERED 1

# Install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Define workdir
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D finally
USER finally
