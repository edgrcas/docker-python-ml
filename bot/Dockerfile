FROM tensorflow:1.9.0-gpu
MAINTAINER Edux <edaniel15@gmail.com>

RUN pip install --upgrade \
  reTexto \
  spacy \
  rasa_nlu[spacy] \
  rasa_core

RUN python -m spacy download es_core_news_sm
RUN python -m spacy link es_core_news_sm es
