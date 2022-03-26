serverless invoke local -f hello -s integration
serverless deploy -s integration
serverless invoke -f hello -l -s integration

## Cloud Formation:

https://us-west-2.console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks?filteringStatus=active&filteringText=&viewNested=true&hideStacks=false

## Parameter Store:

https://us-west-2.console.aws.amazon.com/systems-manager/parameters/?region=us-west-2&tab=Table

## Environment Variables:

https://us-west-2.console.aws.amazon.com/lambda/home?region=us-west-2#/functions/hello?tab=configure
