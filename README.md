# Itemize KID CTF 2020 Challenges:
This is the repo for all the Itemize KID CTF 2020 challenges.

[https://kid2020.itemize.no/](https://kid2020.itemize.no/)

## Structure
The folder structure is `<category>/<challenge>`.

All the challenges contains a `description.md`, this contains the description presented to players on the CTF along with the flag and author.

Challenges with a folder named `<cat>/chall>/files` are files that were presented to the players to download during the CTF.

## Writeups:
All challenges should contain either a `writeup.md` or a folder called `writeup` which has a description of how you could have solved the challenges.

## docker:
Most challenges that were running services, e.g. web servers or pwn applications have a `docker-compose.yml` file which you can start by running `docker-compose up` to start the service localy for testing.