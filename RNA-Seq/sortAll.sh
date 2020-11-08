#!/usr/bin/env bash
# sortAll.sh

#Initialize variable to contain the directory of sorted bam files
bamPath="bam/"
#Initialize variable to contain the suffix for sam files
Suffix=".sam"
#Initialize variable to contain the directory of aligned sam files
InputSam="sam/"
# Create the output directory
mkdir -p $bamPath

#Loop through all the .sam files in $InputSam
function sortAll {
    for alignedFile in $InputSam*$Suffix
    do
        #Remove the path from the filename and assign to pathRemoved
        pathRemoved="${alignedFile/$InputSam/}"
        #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
        sampleName="${pathRemoved/$Suffix/}"
        #Print $sampleName to see what it contains after removing the path
        echo $sampleName
        samtools sort \
        $InputSam${sampleName}.sam \
        -o $bamPath${sampleName}.sorted.bam \
    done
}
sortAll 1>sortAll.log 2>sortAll.err &

