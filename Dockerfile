FROM python:latest
RUN groupadd -r user && useradd -r --create-home --home-dir /home/user -g user user
ADD ./req.txt .
RUN pip3 install -r req.txt

RUN mkdir ./src
ADD ./src /src

WORKDIR src

USER user