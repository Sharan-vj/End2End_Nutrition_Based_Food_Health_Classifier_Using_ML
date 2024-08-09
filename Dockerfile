FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


COPY . /code

WORKDIR /code

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 5000