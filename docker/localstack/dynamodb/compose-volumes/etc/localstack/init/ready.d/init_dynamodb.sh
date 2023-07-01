#!/bin/bash
awslocal dynamodb create-table \
    --table-name TwelveFactorDatastore \
    --key-schema AttributeName=Application,KeyType=HASH \
    --attribute-definitions AttributeName=Application,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region ap-northeast-1

awslocal dynamodb put-item \
    --table-name TwelveFactorDatastore \
    --item '{"Application":{"S":"TwelveFactorApp"},"Name":{"S":"Twelve Factor App"},"Language":{"S":"Python"},"Platform":{"S":"Docker and LocalStack"},"BgColor":{"S":"Brown"}}' \
    --region ap-northeast-1
