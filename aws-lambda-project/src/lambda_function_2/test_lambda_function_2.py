import json
from lambda_function_2.handler import lambda_handler

def test_lambda_handler():
    # Sample event and context
    event = {}
    context = {}

    # Call the Lambda function handler
    response = lambda_handler(event, context)

    # Assert the status code and body in the response
    assert response['statusCode'] == 200
    assert response['body'] == "Function 2 processed the event!"

