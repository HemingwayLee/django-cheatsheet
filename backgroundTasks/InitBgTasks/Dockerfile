FROM python:3.8

RUN apt-get update && apt-get install -y sudo tmux

RUN mkdir -p /home/proj
WORKDIR /home/proj
COPY . .

# `-f` option will remove the db.sqlite3 file no matter the file exists or not
#  use it to prevent errors during docker build time
RUN rm -f db.sqlite3
RUN pip3 install -r requirements.txt


