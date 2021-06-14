FROM python:3.8

RUN apt-get update && apt-get install -y sudo postgresql postgresql-contrib nginx vim

RUN mkdir -p /home/proj
WORKDIR /home/proj
COPY . .

RUN pip3 install -r requirements.txt

RUN cp /home/proj/nginx/default /etc/nginx/sites-enabled/default 

