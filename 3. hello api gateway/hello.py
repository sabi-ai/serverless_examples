import os


def handler(event, context):
    name = "Unknown"
    pathParameters = event.setdefault("pathParameters", None)
    if pathParameters is not None:
        name = pathParameters.setdefault("name", name)

    return {
        "statusCode": 200,
        "body": f"""
            <html>
                <body>
                    <h2>Hi {name}</h2>
                    Based on our records, this is how you look like:</br>
                    <img src="https://www.thispersondoesnotexist.com/image" width="400"><br>
                    BTW, the secret password is: {os.environ['DB_PASSWORD']}
                </body>
            </html>""",
        "headers": {
            "Content-Type": "text/html",
        },
    }
