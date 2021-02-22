FROM alpine

RUN apk update && \
    apk upgrade

RUN apk add python3 && \
    pip3 install flask redis

WORKDIR /data

ENTRYPOINT flask run --host=0.0.0.0
