#!/usr/bin/env python3
# readFastq.py
# Import Seq, SeqRecord, and SeqIO
from Bio import SeqIO
# Import itertools to take a slice of list
import itertools
# The first parameter to SeqIO.parse is the file location
# The second parameter is the file type
leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
# Just get five sequences as an esxample
firstFive = itertools.islice(leftReads, 5)
for left in firstFive:
    print(left.id)

