FROM python:3.8-slim

RUN apt-get update && apt-get -y upgrade && apt-get -y install gcc python3-dev
RUN pip3 install virtualenv

RUN useradd -ms /bin/bash reternal
USER reternal
WORKDIR /home/reternal

ENV VIRTUAL_ENV=/home/reternal/venv
RUN virtualenv -p python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

ADD workers /home/reternal/workers

ENTRYPOINT ["celery", "--app", "workers", "worker", "-Q", "c2"]
