FROM node:alpine

WORKDIR /app
COPY ./src/spa/ .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

ARG API_BASE_URL
ARG MAINTENANCE_MODE

RUN npm install
RUN npm i -g cross-env
RUN npm run ssr