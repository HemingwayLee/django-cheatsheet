#!/bin/bash

cd /home/proj/
python3 manage.py makemigrations main
python3 manage.py migrate

tmux new-session -d -s bgtask1 "python3 manage.py process_tasks --queue do_task"
tmux new-session -d -s bgtask2 "python3 manage.py process_tasks --queue time_report"
python3 manage.py runserver 0.0.0.0:8000
