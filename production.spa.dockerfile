FROM node:alpine as build-stage

WORKDIR /app
COPY ./src/spa/ .

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

ARG API_BASE_URL
ARG MAINTENANCE_MODE

RUN npm install
#RUN npm i -g cross-env
#RUN npm run ssr
RUN npm run build

# build finished here... ready now for production

FROM node:alpine

WORKDIR /app
COPY --from=build-stage /app/static/ ./static/
COPY --from=build-stage /app/express.js ./express.js
COPY --from=build-stage /app/package.express.json ./package.json

RUN npm install