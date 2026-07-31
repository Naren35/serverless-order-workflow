# Serverless-Order-Work_Flow
Production-style event-driven serverless application built with AWS CloudFormation, Lambda, API Gateway, Amazon SQS, SNS, EventBridge, and CloudWatch.

**OPEN MARKET**

================================================================================
                    SERVERLESS ORDER WORKFLOW
              Software Requirements Specification (SRS)
================================================================================

Version        : 1.0
Author         : Narendhiran C
Project Type   : Serverless Cloud Application
Cloud Provider : Amazon Web Services (AWS)
IaC Tool       : AWS CloudFormation (YAML)
Status         : Design Phase

=================================================================================
			overview
=================================================================================

Customer Requirements

• Customers should be able to place an order through a REST API.

• The system must immediately acknowledge a valid order request.

• Every accepted order must receive a unique Order ID.

• Customers must receive meaningful error messages if the order cannot be accepted.

• Order processing should continue in the background after the order is accepted.

• Every accepted order must be traceable using its unique Order ID.

==================================================================================
