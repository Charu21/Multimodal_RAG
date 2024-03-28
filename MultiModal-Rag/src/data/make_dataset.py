import os
import sys
import pandas as pd
import os
import pyarrow as pa
import pickle

from datasets import DatasetDict, load_dataset
from dataclasses import dataclass
from src.logger import logging
from src.exceptions import CustomException

@dataclass
class DataIngestionConfig:
    dataset_to_use: str ="vipulmaheshwari/GTA-Image-Captioning-Dataset"
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def fetch_data(self):
        logging.info("Starting data fetch ...")

        dataset = load_dataset(self.ingestion_config.dataset_to_use) 
    
        try:
            with open('./data/db.pickle', 'wb') as f:  # 'wb' mode overwrites existing file, creates the file if it doesn't exist
                pickle.dump(dataset, f)
        except FileExistsError:
            with open('./data/db.pickle', 'xb') as f:  # 'xb' mode creates a new file for writing, fails if the file already exists
                pickle.dump(dataset, f)
            logging.info('Reading data from '+ self.ingestion_config.dataset_to_use + "is complete")
            
        except Exception as e:
            raise CustomException(e, sys)