FROM python:3.8

RUN apt-get update && apt-get install -y sudo tmux

RUN mkdir -p /home/proj
WORKDIR /home/proj
RUN echo "aaaa"
COPY . .

RUN rm db.sqlite3
RUN pip3 install -r requirements.txt


