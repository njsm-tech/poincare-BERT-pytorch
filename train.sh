WIKIV='2'
DATADIR="data/wikitext${WIKIV}/wikitext-${WIKIV}"

bert-vocab -c $DATADIR/wiki.train.berttokens-shard/* -o $DATADIR/wiki.vocab
bert -c $DATADIR/wiki.train.berttokens-shard/* -t $DATADIR/wiki.valid.berttokens-shard/* -v $DATADIR/wiki.vocab -o $DATADIR/bert.model
