FROM  node:8.11.4-alpine

WORKDIR /app
COPY ./src/spa/package.express.json .

RUN apk update && apk upgrade

RUN npm install
