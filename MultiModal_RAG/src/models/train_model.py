# from dataclasses import dataclass

# import lancedb
# import gradio as gr
# import pickle

# from src.utils import embed_txt

# @dataclass
# class ModelTrainerConfig:

#     class ModelConfig:
#         def __init__(self):
#             with open('./data/db.pickle', 'rb') as f:
#                     self.ds = pickle.load(f)
#             db = lancedb.connect('./data/tables')
#             self.tbl = db.open_table("gta_data")
            
#         def test_model(self, test_data_start, test_data_end):
#             for i in range(test_data_start, test_data_end):
#                  result = self.tbl.search(embed_txt(self.ds["train"][i]["text"]))
                 

# def gta_search(query_str):
    
    
#     db = lancedb.connect('./data/tables')
#     tbl = db.open_table("gta_data")
#     result = tbl.search(embed_txt(query_str)).limit(3).to_pandas()
#     data_id = int(result['id'][0])
#     return ds["train"][data_id]['image'], ds["train"][data_id]["text"]

# interface = gr.Interface(fn= gta_search,
#                         inputs= 'text',
#                         outputs= ['image', 'text'],
#                         title = 'Grand Theft Auto Search Engine',
#                         description = """A Grand Theft Auto Multimodal Retrieval-Augmented Generation (RAG) Application thatleverages LanceDB as a vector database, OpenAI’s “ViT-L/14” for multimodal embedding, and the
# GTA-Image-Captioning-Dataset provided. The application should be capable of processing and
# understanding complex queries related to the Grand Theft Auto universe, providing accurate and
# contextually relevant responses that combine textual and visual information.""")

# interface.launch()