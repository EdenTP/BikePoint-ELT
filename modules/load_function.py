import os
import boto3
import logging

logger=logging.getLogger(__name__)


def bikepoint_load(data_dir,aws_access_key,aws_secret_key,aws_bucket_name):

    
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
