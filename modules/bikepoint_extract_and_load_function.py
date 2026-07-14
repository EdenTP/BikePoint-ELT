from modules.extract_function import bikepoint_extract
from modules.load_function import bikepoint_load



def bikepoint_extract_and_load(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME): 
    
    bikepoint_extract(data_dir)
    bikepoint_load(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME)
    return None

