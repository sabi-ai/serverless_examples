import json
import os
import boto3


def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("usersTable")
    name = "Unknown"
    pathParameters = event.setdefault("pathParameters", None)
    if pathParameters is not None:
        name = pathParameters.setdefault("name", name)

    names = get_names(table)
    put_name(table, name)
    body = f"""
            <html>
                <body>
                    <h2>Hi {name}</h2>
                    Based on our records, this is how you look like:</br>
                    <img src="https://www.thispersondoesnotexist.com/image" width="400"><br>
                    BTW, the secret password is: {os.environ['DB_PASSWORD']}<br><br>
                    <h2>Other Names Using This Service:<h2>"""
    for name_obj in names:
        if name_obj["name"] != name:
            body += f'{name_obj["name"]}<br>'
    body += """</body>
            </html>"""

    return {
        "statusCode": 200,
        "body": body,
        "headers": {
            "Content-Type": "text/html",
        },
    }


def put_name(table, name):
    response = table.put_item(Item={"name": name})
    return response


def get_names(table):
    response = table.scan()
    data = response["Items"]

    while "LastEvaluatedKey" in response:
        response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
        data.extend(response["Items"])

    return data
