import torch.nn as nn

from .poincare import PoincareEmbedding

class SegmentEmbedding(nn.Embedding):
    def __init__(self, embed_size=512):
        super().__init__(3, embed_size, padding_idx=0)

class PoincareSegmentEmbedding(PoincareEmbedding):
    def __init__(self, embed_size=32):
        super().__init__(3, embed_size, padding_idx=0)
