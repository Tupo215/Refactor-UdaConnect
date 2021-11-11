FROM python:3.7

WORKDIR .

COPY ./modules/kafka-consumer/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5002

COPY ./modules/kafka-consumer .
CMD ["python", "__init__.py", "--host", "0.0.0.0"]
