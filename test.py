from configparser import ConfigParser
import time
import signal
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s-%(message)s')
file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def printInfo (fileName,req_key_list,cfg) :

	config = ConfigParser()
	config.read(fileName)
	section_list = config.sections()
	
	for i in section_list:
		lists = config[i]
		for item in lists:
		
			value = config[i][item]
			cfg[item] = value
		
	for req_key in req_key_list :
		logger.debug('cfgkeys :'.format(cfg.keys()))
		if req_key not in cfg.keys():
			return False, 'not finde "' + req_key + '"'		
	logger.info('cfg arry :'.format(cfg))  
	return True, cfg
		
status, result = printInfo('config.ini', ['firstname','lastname'], {'midName':''})

if not status:
	print(result)
	exit(1)
res = result
print('your name is ', res['firstname'],res['midName'],res['lastname'])	
	
def handle_sig(sig, frame):

	print("signal")
	exit(1)
	
signal.signal(signal.SIGINT, handle_sig)
	
while False:
    printInfo()
    time.sleep(1)
    


