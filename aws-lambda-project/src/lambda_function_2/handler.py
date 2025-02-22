from common.utils import log_message

def lambda_handler(event, context):
    log_message('Lambda Function 2 is processing the event.')
    return {
        'statusCode': 200,
        'body': 'Function 2 processed the event!'
    }
