FROM python:3.6

RUN apt-get update && apt-get -y upgrade && apt-get -y install gcc python3-dev

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Make sure to define the JWT_SECRET and FLASK_SECRET in 
# the docker(compose) configuration. ie:
# ENV C2_SECRET


ARG CELERY_BROKER=redis://redis-service:6379
ENV CELERY_BROKER="${CELERY_BROKER}"

ARG CELERY_BACKEND=redis://redis-service:6379
ENV CELERY_BACKEND="${CELERY_BACKEND}"

ARG C2_PORT=8080
ENV C2_PORT="${C2_PORT}"

ARG MONGO_DB=reternal
ENV MONGO_DB="${MONGO_DB}"

ARG MONGO_IP=mongodb
ENV MONGO_IP="${MONGO_IP}"

ARG MONGO_PORT=27017
ENV MONGO_PORT="${MONGO_PORT}"

COPY . /reternal-c2
WORKDIR /reternal-c2

CMD python run.py



