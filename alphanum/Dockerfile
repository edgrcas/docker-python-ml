FROM python:3-slim
MAINTAINER Edux <edaniel15@gmail.com>

RUN pip install -U pip
RUN apt-get update && apt-get install -y \
    build-essential \
    gfortran \
    libblas-dev \
    liblapack-dev \
    libxft-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade \
    reTexto \
    numpy \
    scipy \
    spacy \
    scikit-learn \
    nltk

RUN python -m spacy download es_core_news_sm
RUN python -m spacy link es_core_news_sm es
