FROM alpine:latest

RUN apk add --no-cache python3 bash git rsync

COPY ./src /src
WORKDIR /src

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "./listener.py" ]
