FROM python:3.11.3
USER root

RUN apt-get update
RUN apt-get upgrade -y

ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH /root/.local/bin:$PATH
RUN poetry config virtualenvs.create false

RUN poetry install
