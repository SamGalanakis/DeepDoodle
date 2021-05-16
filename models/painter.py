import torch
import torch.nn as nn
import einops












class Painter(nn.module):
    def __init__(self,image_embedder):
        super().__init__()
        image_embedder = image_embedder()
        for param in image_embedder.params():
            param.requires_grad = False
        self.image_embedder = image_embedder





    def forward(self,image):




