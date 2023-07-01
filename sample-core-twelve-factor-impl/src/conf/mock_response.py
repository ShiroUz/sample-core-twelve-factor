import json
import boto3
import botocore
from io import BytesIO
from pathlib import Path

CONTENT_JSON = {"TableName": "TwelveFactorDatastore"}

def get_configuration_mock_res() -> dict:
    # https://qiita.com/Kept1994/items/1fe3a3d99c3d8f314e46#正常系
    body_encoded = json.dumps(CONTENT_JSON).encode()
    # body_encoded = "{\"aaa\": 3}".encode() # 勿論直接dumps後の文字列を埋めるのでもok
    content_length = len(body_encoded)
    # StreamingBodyへ整形する。
    body = botocore.response.StreamingBody(
        BytesIO(body_encoded),
        content_length
    )
    mock_res = {
        "Content": body,
        "ConfigurationVersion": "dummy",
        "ContentType": "dummy"
        }
    return mock_res
