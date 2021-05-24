WIKIV='2'
DATADIR="./data/wikitext${WIKIV}/wikitext-${WIKIV}"

bert-vocab -c $DATADIR/wiki.train.berttokens -o $DATADIR/wiki.vocab
bert -c $DATADIR/wiki.train.berttokens \
	-t $DATADIR/wiki.valid.berttokens \
	-v $DATADIR/wiki.vocab \
	-o $DATADIR/bert.model \
	--with_cuda true
