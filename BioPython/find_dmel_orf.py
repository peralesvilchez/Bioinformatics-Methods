#!/usr/bin/env python3
# read_seq.py

from Bio import SeqIO
import re
from Bio.Seq import Seq
#dna = Seq("AGTACACTGGTA")
for record in SeqIO.parse("/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta", "fasta"):
#Reading the FASTA file, selecting only chromosomes
      if re.match("^\d{1}\D*$", record.id):
        # Assigning a variable to the record sequence
            dna = record.seq
        #Transcribing DNA
            rna = dna.transcribe()
        # Finding ORF, searching the sequence that starts with AUG and ending with a stop codon (UAA, UAG , or UGA) making sure that have bases of three (codons) between end and start and get the shortest match between start and stop
            orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
         #Translate RNA to protein, make sure to convert orf to a sequence
            protein = Seq(orf).translate()
          #Print the proteins
            print(protein) 
