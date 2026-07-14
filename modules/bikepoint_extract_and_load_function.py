from modules.extract_function import bikepoint_extract
from modules.load_function import bikepoint_load



def bikepoint_extract_and_load(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME): 
    """
    Extract bike point data from the TFL API and upload to S3 Bucket.

    Args:
        data_dir (str): The local directory where the extracted data will be saved and uploaded to S3 from.
        AWS_ACCESS_KEY (str): AWS access key.
        AWS_SECRET_ACCESS_KEY (str): AWS secret key.
        AWS_BUCKET_NAME (str): S3 bucket name.

    Returns:
        None, but extracts and uploads the bikepoint api data to the specified S3 bucket.
    """
    bikepoint_extract(data_dir)
    bikepoint_load(data_dir,AWS_ACCESS_KEY,AWS_SECRET_ACCESS_KEY,AWS_BUCKET_NAME)
    return None

