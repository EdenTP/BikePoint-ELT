import requests as req
from datetime import datetime
import os
import json
import time
import logging

logger=logging.getLogger(__name__)



def bikepoint_extract(data_dir):

    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
   
    logger.info('Logger has lift off')
    os.makedirs('data', exist_ok=True)

    url = 'https://api.tfl.gov.uk/BikePoint/'


    file_name = f'{data_dir}/bike_points_{timestamp}.json' #file name format for saving jsons

    max_retry = 5
    attempt = 0
    delay = 10

    while attempt<=max_retry : #while loop to retry if the API fails to respond or returns a 5xx error
        response = req.get(url)
        data = response.json()
        status=response.status_code
        if 200 <= status < 300 and len(data)>1: #case for successful download of json from API, saves to data folder
                with open(file_name,'w') as file:
                    json.dump(data,file)
                    logger.info(f'success has been suffered {file_name} saved')
                    break
        elif status <= 100 or status>=500: #case for failed download to retry 
            attempt=attempt+1
            logger.info(f'Sus status({status}) waiting to try again, attempt number {attempt+1}')
            time.sleep(delay)
        else : #case for carnage, so we log the status code and json size and break the loop
            logger.info(f'PANIK! status code {status} on attempt {attempt+1}, JSON size {len(data)}')
            break
        return None


