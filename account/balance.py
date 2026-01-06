from common.logger import Logger

import json

logger = Logger('account.balance')

def main(args):
    logger.info('Function was invoked with the following arguments...')
    logger.info(args)

    return {'statusCode': 200, 'body': json.dumps({'coins': 0, 'tokens': 0, 'pending': 0})}

def handler(event, context):
    logger.info(f'Function invocation started...[{context.aws_request_id}]')
    return main(event)
