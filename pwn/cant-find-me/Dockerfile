# sudo docker build -t name .
# sudo docker run -d -p 1024:1024 --rm -it name

FROM ubuntu:20.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY ynetd .
COPY cant-find-me .

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 20000 ./cant-find-me
