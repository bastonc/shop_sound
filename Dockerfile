FROM python:3.10

RUN apt update
RUN python --version

RUN mkdir "shop_sound"

COPY ./src ./shop_sound
COPY ./requirements.txt ./shop_sound

WORKDIR /shop_sound

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "manage.py", "runserver", "0:8008"]
