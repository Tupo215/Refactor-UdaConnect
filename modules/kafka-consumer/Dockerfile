FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY ./modules/kafka-consumer/requirements.txt requirements.txt
RUN pip install -r requirements.txt


EXPOSE 5010

COPY ./modules/kafka-consumer .
CMD ["python", "consumer.py"]