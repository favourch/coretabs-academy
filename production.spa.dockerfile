FROM node:alpine

WORKDIR /app
COPY ./src/spa/ .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN npm install