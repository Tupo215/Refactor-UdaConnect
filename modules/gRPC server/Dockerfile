FROM python:2.7

WORKDIR .

COPY /modules/gRPCpersonID/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5005

COPY ./modules/gRPCpersonID/app .
CMD ["python", "app.py", "--host", "0.0.0.0"]