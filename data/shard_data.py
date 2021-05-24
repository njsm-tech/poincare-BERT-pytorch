import math
import os
import shutil

wikiv = 103
data_dir = "wikitext{v}/wikitext-{v}".format(v=wikiv)
path_template = data_dir + "/wiki.{name}.tokens"
shard_size_bytes = 32 * 1024 * 1024

def make_shards(path):
    size = os.path.getsize(path)
    dirname = path + '-shards'
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.mkdir(dirname)
    num_shards = math.ceil(size / shard_size_bytes)
    with open(path, 'rb') as f:
        for i in range(num_shards):
            shard_path = os.path.join(dirname, 'shard-%d' % i)
            print('making shard %s' % shard_path)
            bytes_ = f.read(shard_size_bytes)
            with open(shard_path, 'wb') as f_shard:
                f_shard.write(bytes_)

def main():
    for name in ('train', 'valid', 'test'):
        path = path_template.format(name=name)
        make_shards(path)

if __name__ == '__main__':
    main()
