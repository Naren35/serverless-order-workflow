import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

table = dynamodb.Table(os.environ["TABLE_NAME"])
TOPIC_ARN = os.environ["TOPIC_ARN"]

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

        # Store order in DynamoDB
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

        # Publish notification to SNS
        message = f"""
Order Processed Successfully

Order ID : {order['orderId']}
Customer : {order['customer']}
Product  : {order['product']}
Quantity : {order['quantity']}

Status : Processed
"""

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="OpenMarket - Order Processed",
            Message=message
        )

        print("SNS notification sent successfully")

    return {
        "statusCode": 200
    }
