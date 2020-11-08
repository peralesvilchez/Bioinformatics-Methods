#!/usr/bin/env python
# read_by_line.py

# Open a sample fastq file for reading
#Import re tu support regular expressions in this program.
import re
import os
read_sample = open('/scratch/SampleDataFiles/Sample.R1.fastq', 'r')

# Initialize a variable to contain the lines
line = ''

# While line is not empty
while line:
    #Read one line from thje file using readline() methid
    line= read_sample.readline()
    #Remove end-of-line character
    line=line.rstrip("\n")
    if re.match('^[ATGCN]+$', line):
        #Print the line
        print(line)

#Close the file using the close () method
