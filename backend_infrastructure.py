```python
import boto3

# AWS S3 for data storage
s3 = boto3.resource('s3')

# AWS DynamoDB for user and product data
dynamodb = boto3.resource('dynamodb')

# AWS Lambda for serverless functions
lambda_client = boto3.client('lambda')

# AWS S3 bucket for data storage
def create_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
    except Exception as e:
        print(e)

# DynamoDB tables for user and product data
def create_table(table_name, key_schema, attribute_definitions):
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_definitions,
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    except Exception as e:
        print(e)

# AWS Lambda function for data manipulation
def create_lambda_function(function_name, runtime, role, handler, code):
    try:
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime=runtime,
            Role=role,
            Handler=handler,
            Code=code,
        )
    except Exception as e:
        print(e)

# Create S3 bucket
create_bucket('ai-personal-shopper-data')

# Create DynamoDB tables
create_table('Users', [{'AttributeName': 'userID', 'KeyType': 'HASH'}], [{'AttributeName': 'userID', 'AttributeType': 'N'}])
create_table('Products', [{'AttributeName': 'productID', 'KeyType': 'HASH'}], [{'AttributeName': 'productID', 'AttributeType': 'N'}])

# Create Lambda functions
create_lambda_function('authenticateUser', 'python3.8', 'arn:aws:iam::123456789012:role/service-role/MyTestFunctionRole', 'authenticateUser.handler', {'ZipFile': open('authenticateUser.zip', 'rb').read()})
create_lambda_function('retrieveData', 'python3.8', 'arn:aws:iam::123456789012:role/service-role/MyTestFunctionRole', 'retrieveData.handler', {'ZipFile': open('retrieveData.zip', 'rb').read()})
create_lambda_function('submitData', 'python3.8', 'arn:aws:iam::123456789012:role/service-role/MyTestFunctionRole', 'submitData.handler', {'ZipFile': open('submitData.zip', 'rb').read()})
create_lambda_function('manipulateData', 'python3.8', 'arn:aws:iam::123456789012:role/service-role/MyTestFunctionRole', 'manipulateData.handler', {'ZipFile': open('manipulateData.zip', 'rb').read()})
```