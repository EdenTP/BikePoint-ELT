import requests as req
from datetime import datetime
import os
import json
import logging
import time
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_dir='logs/extract'
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'
handlers=[
    logging.FileHandler(f"{log_dir}_{timestamp}.log"),  # Saves to file
    logging.StreamHandler()                        # Prints to terminal
]
logging.basicConfig(
    format = '%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=handlers
)

logger=logging.getLogger()
logger.info('Logger has lift off')
os.makedirs('data', exist_ok=True)

url = 'https://api.tfl.gov.uk/BikePoint/'

file_name = f'data/bike_points_{timestamp}.json'
max_retry = 5
attempt = 0
delay = 10

while attempt<=max_retry :
    response = req.get(url)
    data = response.json()
    status=response.status_code
    if 200 <= status < 300 and len(data)>1:
            with open(file_name,'w') as file:
                json.dump(data,file)
                #print('suffering from success')
                logger.info(f'success has been suffered/{file_name} saved')
                break
    elif status <= 100 or status>=500:
        attempt=attempt+1
        logger.info(f'Sus status({status}) waiting to try again, attempt number {attempt+1}')
        time.sleep(delay)
    else : 
        logger.info(f'PANIK! status code {status} on attempt {attempt+1}, JSON size {len(data)}')
        break



