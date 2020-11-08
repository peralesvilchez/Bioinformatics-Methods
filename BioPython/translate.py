#!/usr/bin/env python3
# translate.py
# Import Seq

from Bio.Seq import Seq

dna = Seq("AGTACACTGGTA")
rna = dna.transcribe()
protein = rna.translate()
#myseq=Seq(protein)
SeqIO.write(protein, "protein.fasta", "fasta")
