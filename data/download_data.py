from torchtext.datasets import WikiText2, WikiText103

def main():
    d = WikiText2('wikitext2')
    e = WikiText103('wikitext103')

if __name__ == '__main__':
    main()
