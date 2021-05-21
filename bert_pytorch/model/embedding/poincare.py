import torch.nn as nn
from torch.nn.parameter import Parameter

from geoopt.manifolds import PoincareBall
from geoopt.tensor import ManifoldTensor

init_weights = 1e-3

class PoincareEmbedding(nn.Embedding):
    def __init__(self, *args, **kwargs):
        weight = Parameter(ManifoldTensor(*args, manifold=PoincareBall(), **kwargs))
        super().__init__(*args, weight_=weight, **kwargs)
        self.weight.data.uniform_(-init_weights, init_weights)
