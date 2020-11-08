#!/usr/bin/env bash
quast.py Rhodo/contigs.fasta -o quast_results -t 10 1>quast.log 2>quast.err
