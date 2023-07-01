import os
import uvicorn
from src.helper.config_helper import AppConfigHelper

from fastapi import FastAPI
import boto3
from botocore.exceptions import ClientError

app = FastAPI()

# Attempt to refresh config every 1 hour
CONFIG_REFRESH_TIME = 3600

appconfig = AppConfigHelper(
    os.environ['ConfigApp'],
    os.environ['ConfigEnv'],
    os.environ['ConfigProfile'],
    CONFIG_REFRESH_TIME,  
    os.environ['ConfigClient']
)


@app.get('/')
async def health():
    """
    Health check endpoint for the load balancer to poll
    """
    return "All good !"


@app.get('/hello')
async def hello_world():
    """
    Display hello message using the information from the Dynamo table
    """
    # localstackを利用する場合
    if os.environ['ENV'] == 'local':
        ddb_client = boto3.client(
        'dynamodb', region_name=os.environ['AWS_DEFAULT_REGION'], endpoint_url='http://localstack:4566/')
    # 実リソースにデプロイされた場合
    else:
        ddb_client = boto3.client(
            'dynamodb', region_name=os.environ['AWS_DEFAULT_REGION'])
 
    TABLE_NAME = get_table_name()
    try:
        # print(TABLE_NAME)
        response = ddb_client.get_item(
            TableName=TABLE_NAME,
            Key={'Application': {'S': 'TwelveFactorApp'}})
        return f"<html><body style=\"background-color"\
            f":{response['Item']['BgColor']['S']};color:white;text-align:center\">"\
            f"<p><strong><h1>Hello from {response['Item']['Name']['S']}!</h1></strong></p>"\
            f"<p><h2>Developed with {response['Item']['Language']['S']},"\
            f" deployed with {response['Item']['Platform']['S']}"\
            "</h2></p></body></html>"
    except ClientError as e:
        return response['Error']['Message']


def get_table_name():
    """
     Get table name from App Config
    """
    appconfig.update_config()
    return appconfig.config["TableName"]


@app.get('/table-name')
async def table_name():
    """
     Return table name using API
    """
    return get_table_name()


@app.get('/refresh-config')
async def refresh():
    """
     Force refresh config using the API endpoint
    """
    result = "Config Refreshed" if appconfig.update_config(
        force=True) else "Nothing to refresh"
    return result

# Bind the Flask application to port 80 of the runtime environment
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)

# def main():
#     uvicorn.run("src.app:main", host="0.0.0.0", port=80, reload=True)

# if __name__ == "__main__":
#     main()
