import json
import os


def handler(event, context):
    return {"statusCode": 200, "body": f"Hello World this is the secret D Password: {os.environ['DB_PASSWORD']}"}
