FROM python:3.10

RUN apt update
RUN python --version

# create work directory and copying files of project
RUN mkdir "shop_sound"
COPY ./src /shop_sound

# copy requrements.txt for all dependecies
COPY ./requirements.txt /shop_sound

# create commands directory with sh files
RUN mkdir "commands"
COPY ./commands /commands

# setup work directory
WORKDIR /shop_sound

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["bash"]
