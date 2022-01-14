from configparser import ConfigParser
import time
import signal
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('result.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

def fillArray (fileName,req_key_list,cfg) :
	
	config = ConfigParser()
	config.read(fileName)
	section_list = config.sections()
	if(config.read(fileName) == []):
		
		return False, 'file not found'
	for i in section_list:
		lists = config[i]
		for item in lists:
		
			value = config[i][item]
			cfg[item] = value
		
	for req_key in req_key_list :
		logger.debug('cfg keys : {}'.format(cfg.keys()))
		if req_key not in cfg.keys():
			return False, 'could not find "' + req_key + '"'		
	logger.debug('cfg arry : {}'.format(cfg))  
	return True, cfg
		

def printInfo():
	logger.info('your name is: {} {} {} '.format(res['firstname'],res['midName'],res['lastname']))
	
def handle_sig(sig, frame):
	logger.error('program exploded :(')
	exit(1)
	
def handle_bus(sig, frame):
	logger.setLevel(logging.WARNING)
	
def handle_chld(sig, frame):
	logger.setLevel(logging.DEBUG)
	
status, result = fillArray('config.ini', ['firstname','lastname'], {'midName':''})
if not status:
	print(result)
	exit(1)
res = result
				
signal.signal(signal.SIGINT, handle_sig)
signal.signal(signal.SIGBUS, handle_bus)
signal.signal(signal.SIGCHLD, handle_chld)
	
while True:
    printInfo()
    time.sleep(10)
    
    


    


