import os

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

path_template = 'wikitext2/wikitext-2/wiki.{split}.tokens'

def read_file(path):
    with open(path) as f:
        return f.read()

def filepath(name):
    return path_template.format(split=name)

def read_dataset(name):
    path = filepath(name)
    return read_file(path)

def main():
    tokenizer = Tokenizer(BPE())
    trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
    paths = []
    for name in ('train', 'valid', 'test'):
        paths.append(filepath(name))
    tokenizer.train(files=paths, trainer=trainer)
    tokenizer.save('tokenizers/wikitext2')

if __name__ == '__main__':
    main()
