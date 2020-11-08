#!/usr/bin/env bash
# alignPredicted.sh
blastx -query Trinity.fasta.transdecoder.cds \
-db /blastDB/swissprot \
-outfmt "6 qseqid sacc qlen slen length nident pident evalue stitle" \
-evalue 1e-10 \
1>alignPredicted.txt 2>alignPredicted.err &
