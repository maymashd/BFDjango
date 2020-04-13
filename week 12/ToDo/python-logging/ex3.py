from logging.handlers import RotatingFileHandler
import logging

logger=logging.getLogger('my_loggger')
file_handler=RotatingFileHandler('example3.log',maxBytes=1000,backupCount=10,mode='w')
logger.addHandler(file_handler)

for i in range(20):
    logger.error(f'logger number {i}')
