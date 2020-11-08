#!/usr/bin/env bash
# indexAll.sh
#Initialize variable to contain the directory of indexed bai files 
indexPath="bam/"
#Initialize variable to contain the suffix for sorted bam files
Suffix="sorted.bam"


#Loop through all sorted.bam files in $indexPath

function indexAll {
    for sortedFile in $indexPath*$Suffix
    do
        #Remove the path from the filename and assign to pathRemoved
        pathRemoved="${sortedFile/$indexPath/}"
        #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
        sampleName="${pathRemoved/$Suffix/}"
        #Print $sampleName to see what it contains after removing the path
        echo $sampleName
        samtools index \
        $indexPath${sampleName}.sorted.bam \
        -o $indexPath${$sampleName}.sorted.bai \
    done
    }
indexAll 1>indexAll.log 2>indexAll.err &
