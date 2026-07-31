# IAM Design

## Purpose

The `AcceptOrderLambda` function requires permission to:

- Write execution logs to Amazon CloudWatch Logs.
- Send accepted order messages to the Amazon SQS queue.

To follow the Principle of Least Privilege, the Lambda function is assigned a dedicated IAM Role with only the required permissions.

## Benefits

- Improved security
- Fine-grained access control
- Easier auditing
- Reusable Infrastructure as Code
