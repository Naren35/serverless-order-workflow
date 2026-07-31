import json

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

        print("Order Processed Successfully")

    return {
        "statusCode": 200
    }
