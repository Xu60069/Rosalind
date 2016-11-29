#Counting DNA Nucleotides

def CountDNA(dna):
    counter={'A':0, 'T':0, 'G':0, 'C':0}
    for ch in dna:
        counter[ch] += 1
    print(counter)

CountDNA("ATGCC")
