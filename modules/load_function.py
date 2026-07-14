import os
import boto3
import logging

logger=logging.getLogger(__name__)


def bikepoint_load(data_dir,aws_access_key,aws_secret_key,aws_bucket_name):
    """
    Uploads locally saved bikepoint JSON files to the specified S3 bucket and removes them from local storage.

    Args:
        data_dir (str): The directory where the extracted data will be saved.
        aws_access_key (str): AWS access key.
        aws_secret_key (str): AWS secret key.
        aws_bucket_name (str): S3 bucket name.

    Returns:
        None, but loads the extracted data to a JSON file in the specified S3 bucket.
    """
    
    #setting up aws bucket access
    s3_client=boto3.client(
        's3',
        aws_access_key_id = aws_access_key,
        aws_secret_access_key = aws_secret_key
    )
    # creating for loop to go through extracted jsons load into S3 and remove from local staging
    files=os.listdir('data')
    for file in files:
        file_path=os.path.join(data_dir, file)
        file_name=file
        try :
            s3_client.upload_file(file_path,aws_bucket_name,file_name)#upload of actual file
            logger.info(f'{file} uploaded to S3')
            os.remove(file_path) #remove once uploaded
            logger.info(f'{file} removed from local storage')
        except Exception as e:
            logger.error(f' we are cooked {file} failed to upload to S3')
    return None
