import requests

def lambda_handler(event, context):
    BASE_URL = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return {
        'statusCode': 200,
        'body': response.json()[:3]
    }

    return {
        'statusCode': response.status_code,
        'body': 'failed to fetch'
    }
    
    
