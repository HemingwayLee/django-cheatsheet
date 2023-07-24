#!/bin/bash

cd /home/proj/
python3 manage.py makemigrations bg
python3 manage.py migrate

tmux new-session -d -s bgtask1 "python3 manage.py process_tasks"
tmux new-session -d -s bgtask2 "python3 manage.py process_tasks"
python3 manage.py runserver 0.0.0.0:8000
