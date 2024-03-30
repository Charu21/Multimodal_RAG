Grand_theft_auto search
==============================

## Problem Statement
A Grand Theft Auto Multimodal Retrieval-Augmented Generation (RAG) Application that leverages LanceDB as a vector database, OpenAI’s “ViT-L/14” for multimodal embedding, and the GTA-Image-Captioning-Dataset provided. The application is capable of processing and understanding complex queries related to the Grand Theft Auto universe, providing accurate and contextually relevant responses that combine textual and visual information. 

#### Technologies used:
LanceDB: LanceDB serves as a vector database to handle efficient storage and retrieval of high-dimensional data. 
OpenAI’s “ViT-L/14”: The “ViT-L/14” model is used to create embeddings for images that capture both visual and textual information. 
Hugging Face Dataset: Here have used the “vipulmaheshwari/GTA-Image-Captioning-Dataset” to work on searching appropriate images with query text. 

#### Description:
- The system first ingests data from the GTA-Image-Captioning-Dataset and create multimodal embeddings using “ViT-L/14”. 
- Then, a retrieval system implemented using LanceDB to store and query the embeddings effectively. 
- There are a number of ways to combine the multi modal embeddings of text and image, but here used averaging as results were best according to subjective analysis.

#### Application development:
- The final web app is developed using Gradio for quick development and will be deployed using Huggingface Spaces.
- And for the application project structure cookie-cutter template is used as referenced as explained below.

#### Reference Resources used:
- Multi-Vector Retriever for RAG on tables, text, and images (langchain.dev)
- Multimodal RAG applications - Blixxi Labs (vipul-maheshwari.github.io)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
