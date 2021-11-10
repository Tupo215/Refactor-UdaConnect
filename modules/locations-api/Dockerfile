FROM python:3.7

WORKDIR .

RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY ./modules/locations-api/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5001

COPY ./modules/locations-api .
CMD ["python", "./app/controllers.py", "--host", "0.0.0.0"]
