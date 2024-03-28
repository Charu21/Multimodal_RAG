import logging
from textwrap import wrap
import matplotlib.pyplot as plt
import numpy as np
import clip
import torch

def plot_images(images, captions):
    plt.figure(figsize=(15, 7))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        caption = captions[i]
        caption = "\n".join(wrap(caption, 12))
        plt.title(caption)
        plt.imshow(images[i])
        plt.axis("off")

def embed_image(img, preprocess, model, device):
    processed_image = preprocess(img)
    unsqueezed_image = processed_image.unsqueeze(0).to(device)
    embeddings = model.encode_image(unsqueezed_image)

    # Detach, move to CPU, convert to numpy array, and extract the first element as a list
    result = embeddings.detach().cpu().numpy()[0].tolist()
    return result

def embed_txt(txt):
    device = torch.device("cpu")
    model, preprocess = clip.load("ViT-L/14", device=device)
    logging.info("Model Vit-L/14 loaded!!")
    tokenized_text = clip.tokenize([txt]).to(device)
    embeddings = model.encode_text(tokenized_text)
    
    # Detach, move to CPU, convert to numpy array, and extract the first element as a list
    result = embeddings.detach().cpu().numpy()[0].tolist()
    return result