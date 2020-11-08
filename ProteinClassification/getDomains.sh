#!/usr/bin/env bash
#getDomains.sh
cut -f13 protein.fasta.tsv | sort | uniq > domains.txt
