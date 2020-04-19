import logging

logger=logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler=logging.FileHandler(filename='Logger.txt',mode='w')

formatter=logging.Formatter('%(asctime)s %(levelname)s -- %(message)s ')

handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')