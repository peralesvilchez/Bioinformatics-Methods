#!/usr/bin/env bash
# capture_output.sh
# Specify the input path as an absolute path.
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Specify the desired file suffix
leftSuffix="*R1.fastq"
for fastqFile in $fastqPath$leftSuffix
do
    echo $fastqFile    
    echo $fastqFile 1>out.log 2>out.err
done
