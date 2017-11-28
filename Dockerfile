FROM alpine:latest

RUN apk add --no-cache python3 bash git

COPY ./src /src
WORKDIR /src

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "./listener.py" ]
