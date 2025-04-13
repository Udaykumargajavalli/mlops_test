import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_Exception import CustomException
from utils.common_fucntions import read_yaml
from config.paths_config import *

from google.cloud import storage
from google.oauth2 import service_account

#creds = service_account.Credentials.from_service_account_file("/Users/udaykumargajavalli/Downloads/studious-saga-455906-v3-adef73932668.json")

# set GOOGLE_APPLICATION_CREDENTIALS = path

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config['data_ingestion']
        self.bucket_name = self.config['bucket_name']
        self.file_name = self.config['bucket_file_name']
        self.train_test_ratio = self.config['train_ratio']

        os.makedirs(RAW_DIR, exist_ok = True) #make sure to create if the folder not exists only

        logger.info(f"Data Ingestion started with {self.bucket_name} and file is {self.file_name}")
    

    def download_csv_from_gcp(self):
        try:
            clinet = storage.Client()
            bucket = clinet.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)

            blob.download_to_filename(RAW_FILE_PATH) # downloading to raw directory

            logger.info(f"CSV file is successfully downloaded to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error("Error while downloading the file")
            raise CustomException("Failed to download the csv", e)
    
    def split_data(self):
        try:
            logger.info("Starting the splitting process")

            data = pd.read_csv(RAW_FILE_PATH)
            train_data, test_data = train_test_split(data, test_size = 1 - self.train_test_ratio, random_state=42)
            
            train_data.to_csv(TRAIN_FILE_PATH, index = False)
            test_data.to_csv(TEST_FILE_PATH, index = False)

            logger.info(f"Train data is saved to {TRAIN_FILE_PATH}")
            logger.info(f"Test data is saved to {TEST_FILE_PATH}")
        
        except Exception as e:
            logger.error("Error while splitting the data")
            raise CustomException("Failed to split the data into train test", e)
        
    def run(self):
        try:
            logger.info("Starting data ingestion process")

            self.download_csv_from_gcp()
            self.split_data()

            logger.info("Data Ingestion completed sucessfully")

        except Exception as ce:
            logger.error(f"Custom Exception :", {str(ce)})

        
        finally:
            logger.info("Data ingestion completed finally")


if __name__ == "__main__":
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    


    

            
