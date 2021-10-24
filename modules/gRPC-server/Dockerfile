FROM python:3.7

WORKDIR .

COPY ./modules/gRPC-server/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY ./modules/gRPC-server/app .
CMD ["python", "app.py", "--host", "0.0.0.0"]
