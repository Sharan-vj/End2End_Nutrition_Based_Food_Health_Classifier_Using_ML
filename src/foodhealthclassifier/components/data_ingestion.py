import os
import zipfile
import gdown
import urllib.request as request

from pathlib import Path
from foodhealthclassifier.logging import logger
from foodhealthclassifier.utils.common import get_size
from foodhealthclassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config = DataIngestionConfig):
        self.config = config

    def download_dataset(self):
        try:
            url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs('artifacts/data_ingestion', exist_ok=True)
            logger.info(f'Downloading dataset from {url} into {zip_download_dir}')

            file_id = url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_dir)
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip:
            zip.extractall(unzip_path)