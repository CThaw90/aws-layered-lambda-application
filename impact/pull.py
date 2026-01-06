from common.logger import Logger

logger = Logger('impact.pull')


def main(args, context):
    logger.info('Function was invoked with the following arguments...')
    logger.info(args)


    logger.info('Lambda function was invoked with the following context...')
    logger.info(context)

    return {'statusCode': 200, 'body': 'Lambda function executed successfully'}
