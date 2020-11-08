#!/usr/bin/env bash
# removeStop.sh
head -n500 ~/BINF6308/BLAST/Trinity.fasta.transdecoder.pep | sed 's/[*]//' > protein.fasta
1>protein.fasta.log 2>protein.fasta.err &
