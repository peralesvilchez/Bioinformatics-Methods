Short Read Alignment

##trimAll.sh
This script takes raw input fastq files from `/scratch/Aip/fastq` and uses trimmomatic which is a fast, multithreaded command line tool that can be used to trim and crop Illumina (FASTQ) data to quality control the reads, storing output in 'Paired/'.

#alignAll.sh

This script takes the trimmed Paired reads from trimAll.sh, in "Paired/" and using GSNAP aligned them to the reference GMAP database from Aiptasia genome made by AipBuildindex.sh, and produced a sam file stored in "sam/"
#sortAll.sh
This script uses samtools to sort the aligned sam files from alignAll.sh and convert to a sorted bam files. The bam files are binary and using the samtools view we can check it, they are stored in "bam/"
 
#indexAll.sh
This script uses samtools index command to index the sorted bam files, the files are stored in "bam/" 

References:

[1]Trimmomatic: A flexible read trimming tool for Illumina NGS data 
Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina Sequence Data. Bioinformatics, btu170.
[2]GSNAP
Thomas D. Wu, Serban Nacu, Fast and SNP-tolerant detection of complex variants and splicing in short reads, Bioinformatics, Volume 26, Issue 7, 1 April 2010, Pages 873–881, https://doi.org/10.1093/bioinformatics/btq057
[3]Samtools
*Li H.*, Handsaker B.*, Wysoker A., Fennell T., Ruan J., Homer N., Marth G., Abecasis G., Durbin R. and 1000 Genome Project Data Processing Subgroup (2009) The Sequence alignment/map (SAM) format and SAMtools. Bioinformatics, 25, 2078-9. [PMID: 19505943]
*Li H A statistical framework for SNP calling, mutation discovery, association mapping and population genetical parameter estimation from sequencing data. Bioinformatics. 2011 Nov 1;27(21):2987-93. Epub 2011 Sep 8. [PMID: 21903627]
