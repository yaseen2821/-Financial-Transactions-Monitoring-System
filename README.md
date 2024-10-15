Financial Transactions Monitoring System
Overview
The Financial Transactions Monitoring System is an ETL pipeline designed to monitor and flag potentially fraudulent transactions using Apache Spark and AWS Lambda. This system integrates data from multiple sources, processes large volumes of transaction records, and improves fraud detection capabilities.

Features
ETL Pipeline: Efficiently extracts, transforms, and loads transaction data.
Fraud Detection: Flags transactions that exceed a predefined amount and are classified as withdrawals.
Scalability: Processes over 10 million records daily.
Integration: Utilizes AWS services for a serverless architecture.
Technologies Used
Apache Spark: For large-scale data processing and transformation.
AWS Lambda: For serverless computing to handle data uploads and trigger ETL jobs.
Amazon S3: For data storage and retrieval.
AWS SDK (Boto3): To interact with AWS services programmatically.
Python: The primary programming language used in this project.

Getting Started
Prerequisites
Python 3.x
Apache Spark installed locally or in a cloud environment
AWS account with access to S3 and Lambda services

Running the ETL Pipeline
Modify the etl_pipeline.py to set your S3 bucket name:
input_path = "s3://your-bucket-name/data/transactions.csv"
output_path = "s3://your-bucket-name/output/fraudulent_transactions.csv"

Run the ETL pipeline:
python etl_pipeline.py

Deploying the AWS Lambda Function
Create an S3 bucket in your AWS account to store input and output data.
Create a new Lambda function in the AWS Management Console.
Set up the Lambda function with the necessary IAM permissions to access S3.
Deploy the lambda_function.py code to your Lambda function.
Configure the S3 bucket to trigger the Lambda function on new file uploads.
