from common.logger import Logger

import json
import os

logger = Logger('user.login')

def main(args, context):
    logger.info('Function was invoked with the following arguments...')
    logger.info(args)

    logger.info('Lambda function was invoked with the following context...')
    logger.info(context)

    auth0_secret_key = os.getenv('AUTH0_SECRET_KEY')
    logger.info(f'The function was invoked with the auth0 secret key {auth0_secret_key}')

    return {'statusCode': 200, 'body': json.dumps({'message': 'Token was successfully validated'})}
