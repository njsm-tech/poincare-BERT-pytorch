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
    num_shards = int(math.ceil(size / shard_size_bytes))
    with open(path, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        shard_size_lines = int(math.ceil(num_lines / num_shards))
        for i in range(num_shards):
            shard_path = os.path.join(dirname, 'shard-%d' % i)
            print('making shard %s' % shard_path)
            lower, upper = i*shard_size_lines, min((i+1)*shard_size_lines, num_lines)
            print(lower, upper)
            shard_lines = lines[lower:upper]
            with open(shard_path, 'w') as f_shard:
                f_shard.write('\n'.join(shard_lines))

def main():
    for name in ('train', 'valid', 'test'):
        path = path_template.format(name=name)
        make_shards(path)

if __name__ == '__main__':
    main()
