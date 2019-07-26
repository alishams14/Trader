FROM broccoli:latest

RUN pip install requests ta

COPY . /app

WORKDIR /app

CMD ["python" , "core.py"]
