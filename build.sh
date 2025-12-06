mdkir lib/python

cp -R common lib/python/common

sam build --template-file template.yml
sam deploy --config-env test
