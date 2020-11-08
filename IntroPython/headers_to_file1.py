#!/usr/bin/env python
# open_file.py

import re

# Set the file path to the Drosophila genome
dmel_genome_path = '/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta'

# Initialize a line counter
line_count = 0

# Open the genome file
with open(dmel_genome_path) as dmel_genome:
# Iterate over the lines in the file
            for line in dmel_genome:
# If the line count is less than 50                
                if line_count < 50: 
# Checking the lines with headers
                    if re.match('>', line):
# Increment the line count by one
                          line_count += 1
#Put the result in a txt file
                          print(line)
                          line_to_write = line
                          with open("dmel_headers1.txt", 'a') as out:
                              out.write(line_to_write)
