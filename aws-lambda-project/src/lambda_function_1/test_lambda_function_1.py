import json
from lambda_function_1.handler import lambda_handler
import pytest
import request_mock

def test_lambda_handler():
    # Sample event and context
    event = {}
    context = {}

    # Call the Lambda function handler
    response = lambda_handler(event, context)

    # Assert the status code and body in the response
    assert response['statusCode'] == 201
    assert response['body'] == "post created"

@pytest.fixture
def event():
    '''Mock event'''
    return {}

@pytest.fixture
def context():
    '''mock context'''
    return {}

def test_lambda_handler_failue(requests_mock, event, context):
    '''test failed with 500 internal server error'''
    requests_mock.post("https://jsonplaceholder.typicode.com/posts", statue_code=500)
    response = lambda_handler(event, context)
    assert response["statusCode"] == 500
    assert response["boday"] == "post failed"