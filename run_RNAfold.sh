#!/bin/bash

##Run this script by #Bash run_RNAfold.sh crRNA_and_Targets.fa
##Install RNAfold program from https://www.tbi.univie.ac.at/RNA/RNAfold.1.html

##Input: Fasta file
##Output: tabluar output file from RNAfold program

filename=$1
RNAfold $filename > tmp.txt
perl -pe 's/\n/\t/g; s/>//; s/\s+/\t/; s/\(-/-/; s/\)\t$/\n/' < tmp.txt > tmp2.txt
awk '{ gsub(/\(/,"", $4); print } ' < tmp2.txt > ${filename}_RNAfold.tsv
rm tmp.txt tmp2.txt *_ss.ps

