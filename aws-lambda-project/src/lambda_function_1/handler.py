import requests
from common.utils import log_message

def lambda_handler(event, context):
    log_message('Lambda Function 1 is processing the event.')
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    post_data = {
        "title": "My First Post",
        "body": "This is a simple post",
        "userId": 1
    }

    response = requests.post(BASE_URL, data=post_data)
    if(response.status_code == 201):
        return {
            'statusCode': 201,
            'body': 'post created'
        }


    return {
        'statusCode': response.status_code,
        'body': 'post failed'
    }
