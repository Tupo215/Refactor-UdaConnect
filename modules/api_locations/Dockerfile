FROM python:3.7-alpine

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY ./modules/api_locations/requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN [./modules/api_locations/kafka/bin/zookeeper-server-start.sh config/zookeeper.properties]
RUN [./modules/api_locations/kafka/bin/kafka-server-start.sh config/server.properties]
RUN [./modules/api_locations/kafka/bin/kafka-topics.sh --create --topic locations --bootstrap-server localhost:9092]

EXPOSE 5001

COPY ./modules/api_locations .
CMD ["flask", "run", "--host", "0.0.0.0"]
