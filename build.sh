mkdir -p lib/python

cp -R common lib/python/common

sam build --template-file template.yml
sam deploy --config-env test --parameter-overrides "Auth0SecretKey=${AUTH0_SECRET_KEY}"
