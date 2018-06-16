FROM node:alpine

WORKDIR /app
COPY ./src/spa/package.json .
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN yarn install

COPY ./src/spa/ .
RUN yarn run build