def lambda_handler(event, context):
    print("Hello from Lambdo")
    return {"statusCode": 200, "body": "Hello from Lambda"}
