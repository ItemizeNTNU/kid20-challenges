FROM tiangolo/uwsgi-nginx-flask:python3.8

ENV PYTHONUNBUFFERED=1 \
    # prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


COPY ./app /app