import json
import boto3
from datetime import datetime
import os

dynamodb = boto3.resource("dynamodb")

TABLE_NAME = os.environ["TABLE_NAME"]
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):

    for record in event["Records"]:

        order = json.loads(record["body"])

        print("=" * 50)
        print("Processing Order")
        print("=" * 50)

        print(order)

        table.put_item(
            Item={
                "OrderId": order["orderId"],
                "Customer": order["customer"],
                "Product": order["product"],
                "Quantity": order["quantity"],
                "Status": "Processed",
                "ProcessedTime": datetime.utcnow().isoformat()
            }
        )

        print("Order saved to DynamoDB")

    return {
        "statusCode": 200
    }
