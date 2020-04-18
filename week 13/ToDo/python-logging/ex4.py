import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
hanldler=logging.FileHandler(filename='ex4.log',mode='a')
formatter=logging.Formatter('%(levelname)s -- %(message)s  --%(asctime)s ')
hanldler.setFormatter(formatter)
logger.addHandler(hanldler)



logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')