FROM node:8.11.4-alpine as build-stage

WORKDIR /app
COPY ./src/spa/ .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

ARG API_BASE_URL
ARG MAINTENANCE_MODE

RUN npm install
