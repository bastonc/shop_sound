#!/bin/bash

python manage.py migrate
python manage.py runserver 0:${WSGI_PORT}
