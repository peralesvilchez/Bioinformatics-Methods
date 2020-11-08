#!/usr/bin/env bash
# string_substitution.sh
leftInFile="/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq"
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
fastqSuffix=".fastq"
# Show the variable before substitution
#echo "before: "$leftInFile
# Replace $fastqPath with nothing
pathRemoved="${leftInFile/$fastqPath/}"
#echo "pathRemoved : "$pathRemoved
# Replace $fastqSuffix with nothing
suffixRemoved="${pathRemoved/$fastqSuffix/}"
#echo "suffixRemoved : "$suffixRemoved
# Replace R1 with R2
rightRead="${suffixRemoved/R1/R2}"
#echo "rightRead" $rightRead
