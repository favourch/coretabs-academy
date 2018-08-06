FROM node:alpine

WORKDIR /app
COPY ./src/spa/ .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN npm install
RUN npm i -g cross-env
RUN npm run ssr