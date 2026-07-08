import requests as req
from datetime import datetime
import os
import json
import logging
import time

logging.basicConfig(level=logging.INFO)
os.makedirs('data', exist_ok=True)

url = 'https://api.tfl.gov.uk/BikePoint/'
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'data/bike_points_{timestamp}.json'
max_retry = 5
attempt = 0
delay = 10

#while attempt < max_retry AND 


while attempt<=max_retry :
    response = req.get(url)
    data = response.json()
    status=response.status_code
    
    if 200 <= status < 300:
        with open(file_name,'w') as file:
            json.dump(data,file)
            print('suffering from success')
            break
    elif status <= 100 or status>=500:
        attempt=attempt+1
        print(f'Sus status waiting to try again, attempt number {attempt}')
        time.sleep(delay)
    else : 
        print('panic')
        print(response.status_code)
        break



