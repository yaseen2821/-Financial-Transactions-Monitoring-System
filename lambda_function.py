import json
import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Extract bucket and object details from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Log the event
    print(f"File {key} has been uploaded to bucket {bucket}.")
    
    # Here, you would trigger the Spark job, possibly using AWS Glue, Step Functions, or an EC2 instance.
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully!')
    }
