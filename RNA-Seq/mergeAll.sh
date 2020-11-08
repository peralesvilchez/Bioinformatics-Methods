#!/usr/bin/env bash
# mergeAll.sh
# List the files with ls and redirect (>) the output to bamIn.txt

ls /scratch/AiptasiaMiSeq/bam/*.sorted.bam > bamIn.txt
# Merge the files using bamIn.txt with the -b option

samtools merge -b bamIn.txt bam/AipAll.bam \
1>bam/merge.log 2>bam/merge.err &
