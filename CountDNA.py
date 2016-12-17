#Counting DNA Nucleotides
#http://rosalind.info/problems/dna/

def CountDNA(dna):
    counter={'A':0, 'T':0, 'G':0, 'C':0}
    for ch in dna:
        counter[ch] += 1
    print(counter)

CountDNA("ATGCC")
dna = input("provide your DNA sequence\n")
CountDNA(dna)
