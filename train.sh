WIKIV='103'
DATADIR="./data/wikitext${WIKIV}/wikitext-${WIKIV}"

bert-vocab -c $DATADIR/wiki.train.berttokens-shards/* -o $DATADIR/wiki.vocab
bert -c $DATADIR/wiki.train.berttokens-shards/* \
	-t $DATADIR/wiki.valid.berttokens-shards/* \
	-v $DATADIR/wiki.vocab \
	-o $DATADIR/bert.model \
	--with_cuda true
