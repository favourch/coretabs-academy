FROM coretabsacademy/academy_spa_builder as build-stage

ARG API_BASE_URL
ARG MAINTENANCE_MODE

RUN node --max_old_space_size=8192
RUN npm run build

#RUN npm i -g cross-env
#RUN npm run ssr

# build finished here... ready now for production

FROM coretabsacademy/academy_spa_launcher

WORKDIR /app
COPY --from=build-stage /app/static/ ./static/
COPY --from=build-stage /app/express.js ./express.js