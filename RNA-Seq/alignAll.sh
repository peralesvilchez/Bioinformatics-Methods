#!/usr/bin/env bash
# alignAll.sh
#Initialize variable to contain the directory of aligned files
samPath="sam/"
#Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
#Initialize variable to contain the directory of trimmed fastq files
pairedInput="Paired/"
# Create the output directory
mkdir -p $samPath
#Loop through all the left-read trimmed files in $pairedInput

function alignAll {
    for trimmedFile in $pairedInput*$leftSuffix
    do
        #Remove the path from the filename and assign to pathRemoved
        pathRemoved="${trimmedFile/$pairedInput/}"
        #Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
        sampleName="${pathRemoved/$leftSuffix/}"
        #Print $sampleName to see what it contains after removing the path
        echo $sampleName
        nice -n19 gsnap \
        -A sam \
        -D . \
        -d AiptasiaGmapDb \
        -s AiptasiaGmapIIT.iit \
        $pairedInput$sampleName$leftSuffix \
        $pairedInput$sampleName$rightSuffix \
        1>$samPath${sampleName}.sam
    done
}
alignAll 1>alignAll.log 2>alignAll.err &
