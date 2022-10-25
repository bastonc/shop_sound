#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0:${WSGI_PORT}