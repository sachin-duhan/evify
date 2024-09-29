# namiz/config/config.py
import os
from dotenv import load_dotenv
from namiz.models import DOMAIN

# Load environment variables from .env file
load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/eve_playground')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME', 'your-s3-bucket-name')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'your-access-key')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'your-secret-key')
    AWS_REGION = os.getenv('AWS_REGION', 'your-region')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    DOMAIN = DOMAIN
