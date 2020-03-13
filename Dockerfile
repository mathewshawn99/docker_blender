FROM python:3.6

# copy all the files to the container
COPY . .

RUN apt-get update && yes | apt-get upgrade

RUN wget -q https://download.blender.org/release/Blender2.79/blender-2.79-linux-glibc219-x86_64.tar.bz2

RUN tar -xvf blender-2.79-linux-glibc219-x86_64.tar.bz2

RUN apt-get install libglu1-mesa libxi6 libgconf-2-4 -y

RUN mv blender-2.79-linux-glibc219-x86_64 blender_install

EXPOSE 8888

