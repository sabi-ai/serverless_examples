serverless invoke local -f hello -s integration
serverless deploy -s integration
serverless invoke -f hello -l -s integration

# Install the plugin:

npm install serverless-domain-manager

## route53:

https://us-east-1.console.aws.amazon.com/route53/v2/hostedzones#

## Certificate Manager:

https://us-west-2.console.aws.amazon.com/acm/home?region=us-west-2#/certificates/list
