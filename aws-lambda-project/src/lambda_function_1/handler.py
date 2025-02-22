from common.utils import log_message

def lambda_handler(event, context):
    log_message('Lambda Function 1 is processing the event.')
    return {
        'statusCode': 200,
        'body': 'Function 1 processed the event!'
    }
