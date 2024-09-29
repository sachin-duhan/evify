# namiz/routes/upload.py
from flask import Blueprint, request, jsonify
from namiz.utils.s3_upload import upload_to_s3
from namiz.config import Config
from namiz.utils.logger import get_logger

upload_bp = Blueprint('upload', __name__)
logger = get_logger("upload")

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    logger.info("Received a file upload request.")
    
    if 'file' not in request.files:
        logger.warning("No file part in the request.")
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        logger.warning("No selected file.")
        return jsonify({'error': 'No selected file'}), 400

    logger.info(f"Uploading file: {file.filename}")
    file_url = upload_to_s3(file, Config.S3_BUCKET_NAME)

    if file_url:
        logger.success(f"File uploaded successfully: {file_url}")
        return jsonify({'file_url': file_url}), 200
    else:
        logger.error("File upload failed.")
        return jsonify({'error': 'File upload failed'}), 500
