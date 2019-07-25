FROM broccoli:latest

COPY . /app

WORKDIR /app

CMD ["python" , "core.py"]
