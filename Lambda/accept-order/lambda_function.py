import json
import uuid
import boto3
import os

sqs = boto3.client("sqs")

QUEUE_URL = os.environ["QUEUE_URL"]

def lambda_handler(event, context):

    body = json.loads(event["body"])

    order = {
        "orderId": str(uuid.uuid4()),
        "customer": body["customer"],
        "product": body["product"],
        "quantity": body["quantity"]
    }

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(order)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order accepted successfully",
            "orderId": order["orderId"]
        })
    }
