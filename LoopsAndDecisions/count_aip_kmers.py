#!/usr/bin/env python
# count_aip_kmers.py
# Open a sample fastq file for reading.
# Import re to support regular expressions in this program.
import re
import os
read_sample = open('/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq', 'r')
kmer_length = 6
# Initialize a k-
kmer_dictionary = {}




# Initialize a variable to contain the lines
line = ' '

# While line is not empty
while line:
    # Read one line from the file
    line = read_sample.readline()
    # Remove end-of-line character
    line = line.rstrip(os.linesep)
    if re.match('^[ATGCN]+$', line):
        stop = len(line) - kmer_length + 1        
# Iterate over the positions
        for start in range(0,len(line)-kmer_length+1):
# Get the substring at a specific start and end position
            kmer = line[start:start + kmer_length]
# See if it's in the dictionary
            if kmer in kmer_dictionary:
# Add one to the count
                kmer_dictionary[kmer] += 1
            else:
                # It's not in the dictionary so add with a count of 1
                kmer_dictionary[kmer] = 1
#
read_sample.close()

outfile=open("aip_kmers.txt",'w')
for kmer in kmer_dictionary:
    outfile.write("{}\t{}\n".format(kmer, kmer_dictionary[kmer]))
    #    print(kmer_dictionary["CAGACA"])
outfile.close()
