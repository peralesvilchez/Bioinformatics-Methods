#!/usr/bin/env python
# get_all_kmers.py
seq = 'GCCGGCCCTCAGACAGGAGTGGTCCTGGATG'
stop = len(seq)
for start in range (0,stop):
    kmer = seq[start:start+7]
    print(kmer)
