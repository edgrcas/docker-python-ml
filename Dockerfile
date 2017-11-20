FROM python:3-slim
MAINTAINER Edux <edaniel15@gmail.com>

RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libxft-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade \
    numpy \
    scipy \
    scikit-learn \
    nltk

COPY ./download.py ./
RUN python download.py
