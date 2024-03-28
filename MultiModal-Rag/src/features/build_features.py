import clip
import torch
import os
import pyarrow as pa
import lancedb
import tqdm
import sys
import pickle

from dataclasses import dataclass
from src.utils import embed_image
from src.utils import embed_txt
from src.data.make_dataset import DataIngestion
from datasets import load_dataset
from src.logger import logging
# import logging
from src.exceptions import CustomException

@dataclass
class FeaturesConfig:
     device: str = torch.device("cpu")

class DataProcessor:
    def __init__(self):
        self.data_processor_config = FeaturesConfig()

    def create_vector_table(self):
        db = lancedb.connect('./data/tables')
        schema = pa.schema(
        [
            pa.field("vector", pa.list_(pa.float32(), 768)),
            pa.field("text", pa.string()),
            pa.field("id", pa.int32())
        ])
        tbl = db.create_table("gta_data", schema=schema, mode="overwrite")
        logging.info("Lance table successfully created!!")
        return tbl

    
    def create_embeddings(self, ds, tbl):
        print("Inside create_embeddings function...")
        model, preprocess = clip.load("ViT-L/14", device=self.data_processor_config.device)
        logging.info("Model Vit-L/14 loaded!!")
    
        logging.info("Embeddings creation started....")
        data = []
        for i in range(len(ds["train"])):
            img = ds["train"][i]['image']
            text = ds["train"][i]['text']

            # Element  wise addition of encoded image and text
            combined_embedding = ((torch.tensor(embed_image(img)) + torch.tensor(embed_txt(text))) / 2).tolist()
            data.append({"vector": combined_embedding, "text": text, "id" : i})
            print(f'Done for i= {i}')
        tbl.add(data)
        tbl.to_pandas()
        logging.info("Vector Embeddings successfully created!!!")
    
if __name__ == '__main__':
    try:
        print("Inside ")
        data_ingestion = DataIngestion()
        data_ingestion.fetch_data()
        
        with open('./data/db.pickle', 'rb') as f:
            ds = pickle.load(f)

        print("Now creating table and embeddings")
        obj = DataProcessor()
        tbl = obj.create_vector_table()
        print(f"Vector table = {tbl} created!")

      
        
        obj.create_embeddings(ds, tbl)
        print("back")

    except Exception as e:
            raise CustomException(e, sys)