serverless invoke local -f hello -s integration
serverless deploy -s integration
serverless invoke -f hello -l -s integration

# Install the plugin:

npm install serverless-domain-manager

## DynamoDB:

https://us-west-2.console.aws.amazon.com/dynamodbv2/home?region=us-west-2#tables
