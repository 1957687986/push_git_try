import torch
from torch import nn
from torchnlp.word_to_vector import GloVe

word_to_ix = {"hello": 0, "world": 1}

lookup_tensor = torch.tensor([word_to_ix["hello"]],dtype=torch.long)

embeds = nn.Embedding(2, 5)

hello_embed = embeds(lookup_tensor)

print(hello_embed)

print("-"*100)

vectors = GloVe()

print(vectors["hello"])

