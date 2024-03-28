from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A Grand Theft Auto Multimodal Retrieval-Augmented Generation (RAG) Application that leverages LanceDB as a vector database, OpenAI’s “ViT-L/14” for multimodal embedding, and the GTA-Image-Captioning-Dataset.',
    author='charusmita',
    license='MIT',
)
