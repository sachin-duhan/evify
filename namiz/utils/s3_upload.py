# namiz/utils/s3_upload.py
import boto3
from botocore.exceptions import NoCredentialsError
from namiz.config import Config
from namiz.utils.logger import get_logger

logger = get_logger("s3_upload")

# Initialize boto3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION
)

def upload_to_s3(file, bucket_name, object_name=None):
    if object_name is None:
        object_name = file.filename

    try:
        logger.info(f"Uploading {object_name} to bucket {bucket_name}.")
        s3_client.upload_fileobj(file, bucket_name, object_name)
        file_url = f"https://{bucket_name}.s3.{Config.AWS_REGION}.amazonaws.com/{object_name}"
        logger.info(f"File uploaded successfully. URL: {file_url}")
        return file_url
    except NoCredentialsError:
        logger.error("AWS credentials not available.")
        return None
    except Exception as e:
        logger.error(f"Error uploading to S3: {e}")
        return None
