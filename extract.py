import requests as req
from datetime import datetime
import os
import json
import logging
import time

logging.basicConfig(level=logging.INFO)
url = 'https://api.tfl.gov.uk/BikePoint/'
data_dir = os.makedirs('data', exist_ok=True)
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
file_name = f'data/bike_points_{timestamp}.json'
max_retry = 5
attempt = 0
delay = 10

#while attempt < max_retry AND 
response = req.get(url)
data = response.json()

with open(file_name,'w') as file:
    json.dump(data,file)


