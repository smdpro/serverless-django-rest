import boto3.exceptions
import botocore
import environ
import os 

env = environ.Env()
env.read_env(env_file='.env.dev')

def create_table():

    dynamodb=boto3.resource("dynamodb", region_name=os.environ.get('REGIN_NAME'), endpoint_url=os.environ.get('ENDPOINT_URL'))
    table = dynamodb.create_table(
        TableName = os.environ.get('TABLE'),
        KeySchema = [
            {
                "AttributeName": "id", 
                "KeyType": "HASH"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "id", 
                "AttributeType": "S"
            },
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5, 
            "WriteCapacityUnits": 2
        },
    )
    return table


if __name__ == "__main__":
    try:
        my_table = create_table()
        my_table.meta.client.get_waiter("table_exists").wait(TableName=os.environ.get('TABLE'))
        print("Table was created successfully.")

    except botocore.exceptions.ClientError as error:
        if error.response["Error"]["Code"] == "ResourceInUseException":
            print("Error: This table already exists. please change the table name.")
        else:
            raise error
