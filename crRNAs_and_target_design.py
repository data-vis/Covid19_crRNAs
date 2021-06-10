## This python script takes will reproduce the data published in this publication "Title: Reprogrammed CRISPR-Cas13b suppresses the replication of SARS-CoV-2 variants and circumvents their mutational escape through mismatch tolerance"

## Input: DNA/RNA sequnece file from command line 
## Output: 30 nucleotide long crRNA and Target sequneces for the given input sequence file. Displyed in 4 columns

## Output sequnces and be filtered further to filter crRNAs "PolyT" sequneces (TTTT) by using this command
## python crRNAs_and_target_design.py seq.txt | awk -F'\t' '$2!~/TTTT/' > crRNA_Targets_polyT_removed.tsv


import sys, os

f = open(sys.argv[1],"r")
a=f.read()

sys.stdout = open("crRNA_and_Targets.fa", "w")

alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'U': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a', 'u': 'a', 'N': 'N'} 


def reverse_complement(seq):    
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases


b = [a[i:i+30] for i in range(len(a)-30)]
i = 1
for elem in b:
    print(">crRNA_" + str(i)  + "_" + str(i + 29)) 
    print(reverse_complement(elem))  
    i = i + 1

i = 1
for elem in b:
    print(">Target_" + str(i) + "_" + str(i + 29))
    print(elem)
    i = i + 1


####
##Run RNAfold program


f.close()
