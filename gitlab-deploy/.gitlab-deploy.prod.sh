# !/bin/bash

# Get servers list:
set - f
# Variables from GitLab server:
# Note: They can't have spaces!!
string=$DEPLOY_SERVER
array=(${string//,/ })

# Iterate servers for deploy and pull last commit
# Careful with the ; https://stackoverflow.com/a/20666248/1057052
for i in "${!array[@]}"; do
  echo "Deploy project on server ${array[i]}"
  ssh ubuntu@${array[i]} <<EOF
  export HOST_ENV=$HOST_ENV \
            API_BASE_URL=$API_BASE_URL \
            SPA_BASE_URL=$SPA_BASE_URL \
            DATABASE_URL=$DATABASE_URL \
            DEFAULT_FROM_EMAIL=$DEFAULT_FROM_EMAIL \
            DISCOURSE_API_KEY=$DISCOURSE_API_KEY \
            DISCOURSE_API_USERNAME=$DISCOURSE_API_USERNAME \
            DISCOURSE_BASE_URL=$DISCOURSE_BASE_URL \
            DISCOURSE_SSO_SECRET=$DISCOURSE_SSO_SECRET \
            EMAIL_HOST=$EMAIL_HOST \
            EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD \
            EMAIL_HOST_USER=$EMAIL_HOST_USER \
            MANAGERS_EMAILS=$MANAGERS_EMAILS \
            SECRET_KEY=$SECRET_KEY \
            SENTRY_DSN=$SENTRY_DSN \
            POSTGRES_DB=$POSTGRES_DB \
            POSTGRES_USER: $POSTGRES_USER \
            POSTGRES_PASSWORD: $POSTGRES_PASSWORD \
            MAINTENANCE_MODE='0'

  cd /var/academy
  git stash 
  sudo git checkout $CI_BUILD_REF_NAME
  git stash
  sudo git pull origin master 
  docker-compose -f docker-compose.production.yml up --force-recreate --build -d
EOF
done