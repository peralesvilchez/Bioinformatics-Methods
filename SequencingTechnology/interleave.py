#!/usr/bin/env python3
# readFastq.py
# Import Seq, SeqRecord, and SeqIO
from Bio import SeqIO
# The first parameter to SeqIO.parse is the file location
# The second parameter is the file type
leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
rightReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")
#Open a empty list
myreads = []
#Iterate over left Reads and right Reads
for left, right in zip(leftReads, rightReads):
#Adding elements to the list
    myreads.append(left)
    myreads.append(right)
#Writing a fastq file
SeqIO.write(myreads, "interleaved.fastq", "fastq")
