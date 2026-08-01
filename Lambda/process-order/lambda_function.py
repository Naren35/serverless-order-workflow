import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(os.environ["TABLE_NAME"])

def lambda_handler(event, context):

    for record in event["Records"]:

        order = json.loads(record["body"])

        print("=" * 50)
        print("Processing Order")
        print("=" * 50)

        print(f"Order ID : {order['orderId']}")
        print(f"Customer : {order['customer']}")
        print(f"Product  : {order['product']}")
        print(f"Quantity : {order['quantity']}")

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

        print("Order stored successfully in DynamoDB")

    return {
        "statusCode": 200
    }
