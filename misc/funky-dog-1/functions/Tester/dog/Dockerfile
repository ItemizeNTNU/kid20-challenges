FROM openfaas/classic-watchdog:0.18.8 as watchdog

FROM alpine:3.11

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
COPY /dog /home/app/dog
RUN chmod +x /usr/bin/fwatchdog

ENV fprocess="xargs cat"

RUN addgroup -g 1000 -S app && adduser -u 1000 -S app -G app
USER 1000

CMD [ "/usr/bin/fwatchdog"]
