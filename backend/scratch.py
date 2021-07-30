import boto3

client = boto3.client('ssm', 'us-east-1')

response = client.get_parameter(
    Name='zendesk-token',
    WithDecryption=False
)

print(response['Parameter']['Value'])