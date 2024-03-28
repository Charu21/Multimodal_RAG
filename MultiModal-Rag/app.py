import lancedb
import gradio as gr
import pickle

from src.utils import embed_txt

with open('./data/db.pickle', 'rb') as f:
    ds = pickle.load(f)
db = lancedb.connect('./data/tables')
tbl = db.open_table("gta_data")

def gta_search(query_str):       
    result = tbl.search(embed_txt(query_str)).limit(3).to_pandas()
    data_id = int(result['id'][0])
    return ds["train"][data_id]['image'], ds["train"][data_id]["text"]

interface = gr.Interface(fn= gta_search,
                        inputs= 'text',
                        outputs= ['image', 'text'],
                        title = 'Grand Theft Auto Search Engine',
                        description = """A Grand Theft Auto Multimodal Retrieval-Augmented Generation (RAG) Application thatleverages LanceDB as a vector database, OpenAI’s “ViT-L/14” for multimodal embedding, and the
GTA-Image-Captioning-Dataset provided. The application is capable of processing and
understanding complex queries related to the Grand Theft Auto universe, providing accurate and
contextually relevant responses that combine textual and visual information.""")

interface.launch()