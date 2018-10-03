FROM coretabsacademy/academy_spa_base as build-stage

ARG API_BASE_URL
ARG MAINTENANCE_MODE

RUN node --max_old_space_size=8192
RUN npm run build

#RUN npm i -g cross-env
#RUN npm run ssr

# build finished here... ready now for production

FROM node:8.11.4-alpine

WORKDIR /app
COPY --from=build-stage /app/static/ ./static/
COPY --from=build-stage /app/express.js ./express.js
COPY --from=build-stage /app/package.express.json ./package.json

RUN npm install
