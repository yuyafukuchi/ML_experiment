FROM python:3.8.0
WORKDIR /home/app
RUN apt-get update \
    && apt-get upgrade -y \
    # imageのサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install pipenv

COPY Pipfile Pipfile.lock /home/app/
RUN pipenv install
