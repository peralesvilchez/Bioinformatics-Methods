#!/usr/bin/env python
# join.py
# Define the separator character
sep = "|"

# A sample kmer to use in this join 
kmer = 'ATGCC'
#A sample count
count = 2
# Convert the count to a string 
str_count = str(count)
#Put the kmer and count i a tuple
kmer_count = (kmer,str_count)
# Join the elements of the array with the separator and save in a string
joined_string = sep.join(kmer_count)

# Print the result
print(joined_string)
