# sudo docker build -t name .
# sudo docker run -d -p 20001:20001 --rm -it name

FROM ubuntu:14.04

RUN apt-get update

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY ynetd .
COPY flag.txt .
COPY pwn13 .

RUN chown -R root:root /home/ctf

USER ctf
CMD ./ynetd -p 20002 ./pwn13
