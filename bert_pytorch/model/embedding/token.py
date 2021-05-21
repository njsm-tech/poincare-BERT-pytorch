import torch.nn as nn

from .poincare import PoincareEmbedding

class TokenEmbedding(nn.Embedding):
    def __init__(self, vocab_size, embed_size=512):
        super().__init__(vocab_size, embed_size, padding_idx=0)

class PoincareTokenEmbedding(PoincareEmbedding):
    def __init__(self, vocab_size, embed_size=32):
        super().__init__(vocab_size, embed_size, padding_idx=0)
