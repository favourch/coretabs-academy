FROM node:8.11.4-alpine as build-stage

WORKDIR /app
COPY ./src/spa/ .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN npm install
