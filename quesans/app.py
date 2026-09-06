import torch
import json
import numpy as np
from transformers import pipeline


response_headers = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Credentials": True,
}


nlp = pipeline('question-answering', model = '/opt/ml/model', tokenizer='/opt/ml/model')



def handle_request(event, context):
    print(f"Lambda function ARN: {context.invoked_function_arn}")
    print(f"Lambda funtion version: {context.function_version}")
    print(f"Lambda Request ID: {context.aws_request_id}")

    print(f"Got event", event)

    raw_string = r'{}'.format(event['body'])
    body = json.loads(raw_string)
    originaltext = body['text']
    #originaltext = event['text']
    try:
        print(originaltext)
        res = nlp(originaltext)        
        final = {'output':res}
        print(final)

        print(f">>>> Lambda time remaining in MS: {context.get_remaining_time_in_millis()} >>>>")

        return {
            "statusCode": 200,
            "headers": response_headers,
            "body": json.dumps(final),
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "headers": response_headers,
            "body": json.dumps({"message": "Failed to process image: {}".format(e)}),
        }