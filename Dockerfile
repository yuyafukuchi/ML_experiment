FROM python:3.6.0

RUN apt-get update \
    && apt-get upgrade -y \
    # imageのサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # pipのアップデート
    && pip install --upgrade pip

# 作業するディレクトリを変更
WORKDIR /home/ML_experiment
COPY requirements.txt ${PWD}
RUN pip install -r requirements.txt
# 作業するディレクトリを変更
# コンテナの内部には入った際のディレクトリの位置を変更している

