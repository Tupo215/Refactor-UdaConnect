FROM python:3.7

WORKDIR .

COPY ./modules/gRPC-server/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY ./modules/gRPC-server .
CMD ["python", "__init__.py"]
