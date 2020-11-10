FROM python:3

WORKDIR /app

COPY ynetd .
COPY app.py .

CMD ./ynetd -p 3000 "python3 -u app.py"
