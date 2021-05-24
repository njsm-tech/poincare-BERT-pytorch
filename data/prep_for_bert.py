import re

wikiv = 103
base_dir = "wikitext{v}/wikitext-{v}".format(v=wikiv)
path_template = base_dir + "/wiki.{name}.tokens"
out_path_template = base_dir + "/wiki.{name}.berttokens"

def process(name):
    path = path_template.format(name=name)
    with open(path) as f:
        content = f.read()
    content = re.sub('[\n\t]+', ' ', content)
    sentences = content.split(' . ')
    lines_out = []
    for i in range(0, len(sentences), 2):
        if i + 2 > len(sentences):
            break
        [s0, s1] = sentences[i:i+2]
        lines_out.append("{} . \t{} .".format(s0, s1))
    out = '\n'.join(lines_out)
    out_path = out_path_template.format(name=name)
    with open(out_path, 'w') as f:
        f.write(out)

def main():
    for name in ('train', 'valid', 'test'):
        process(name)

if __name__ == '__main__':
    main()
