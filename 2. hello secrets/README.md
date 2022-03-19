serverless invoke local -f hello -s integration
serverless deploy -s integration
serverless invoke -f hello -l -s integration

## Environment Variables:

https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions/hello?tab=configure
