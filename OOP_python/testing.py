import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
logging.debug('This is Debug')
logging.info('This is info')
logging.warning('This is warning')
logging.error('This is error')
logging.critical('This is critical')

import helper
log_h = logging.FileHandler('testing.log')

fmat = logging.Formatter()
log_h.setFormatter(fmat)