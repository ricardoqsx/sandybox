FROM python:alpine

WORKDIR /src

RUN apk add --no-cache \
    gcc \
    musl-dev \
    mariadb-connector-c-dev \
    python3-dev

COPY ./src .

RUN pip install --no-cache-dir -r req.txt

CMD ["python3", "run.py"]