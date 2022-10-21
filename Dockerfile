FROM python:3.10


# Creating direcory /shop_sound for code of project and /commands for scripts with commands
RUN mkdir /shop_sound && mkdir /commands

# Copying requrements.txt for all dependecies
COPY ./requirements.txt /shop_sound


WORKDIR /shop_sound

# Upgrade pip and installing dependencies
RUN python -m pip install --upgrade pip -r requirements.txt

CMD ["bash"]
