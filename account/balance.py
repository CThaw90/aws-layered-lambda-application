from common.logger import Logger

import json

logger = Logger('account.balance')

def main(args, context):
    logger.info('Function was invoked with the following arguments...')
    logger.info(args)

    logger.info('Lambda function was invoked with the following context...')
    logger.info(context)

    return {'statusCode': 200, 'body': json.dumps({'coins': 0, 'tokens': 0, 'pending': 0})}
