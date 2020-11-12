From python:3
WORKDIR /app
ADD ./requirements.txt .
RUN pip install -r ./requirements.txt
ADD ./app . 
CMD ["python", "-u", "app.py"]