import os
from dotenv import load_dotenv
from datetime import datetime
from modules.log_function import log_config
from modules.extract_function import bikepoint_extract
from modules.bikepoint_extract_and_load_function import bikepoint_extract_and_load



timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
log_dir = 'logs'

logger=log_config(timestamp,log_dir)
logger.info('Logger has lift off')

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME=os.getenv('AWS_BUCKET_NAME')
data_dir='data'

bikepoint_extract_and_load(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME)

