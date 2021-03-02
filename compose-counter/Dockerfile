FROM alpine

RUN apk update && \
    apk upgrade

RUN apk add python3 py3-pip && \
    pip3 install flask redis

WORKDIR /data

ENTRYPOINT flask run --host=0.0.0.0
