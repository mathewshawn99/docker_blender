FROM nvidia/cuda:10.0-devel-ubuntu18.04

# copy all the files to the container
COPY . .

RUN apt-get update && yes | apt-get upgrade

RUN apt-get install wget -y
RUN apt-get install libglu1-mesa libxi6 libgconf-2-4 -y
RUN apt-get install libfontconfig1 libxrender1 -y

RUN wget -q https://download.blender.org/release/Blender2.79/blender-2.79-linux-glibc219-x86_64.tar.bz2

RUN tar -xvf blender-2.79-linux-glibc219-x86_64.tar.bz2



RUN mv blender-2.79-linux-glibc219-x86_64 blender_install

VOLUME /media

ENTRYPOINT ["blender_install", "-b"]

