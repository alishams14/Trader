FROM broccoli:latest

RUN pip install requests pandas

COPY . /app

WORKDIR /app

CMD ["python" , "core.py"]

FROM broccoli:latest

RUN pip install requests pandas

COPY . /app

WORKDIR /app

CMD ["python" , "util.py"]

FROM broccoli:latest

RUN pip install requests pandas

COPY . /app

WORKDIR /app

CMD ["python" , "trend.py"]

FROM broccoli:latest

RUN pip install requests pandas

COPY . /app

WORKDIR /app

CMD ["python" , "temp.py"]

FROM broccoli:latest

RUN pip install requests pandas

COPY . /app

WORKDIR /app

CMD ["python" , "momentum.py"]

FROM broccoli:latest

RUN pip install requests pandas

COPY . /app

WORKDIR /app

CMD ["python" , "candle_ogoly.py"]
