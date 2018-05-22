import Bio
from Bio import SeqIO

def splitter(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def repeats(pattern, threshold):
    p = list(splitter(dna_seq, len(pattern)))
    res = {}
    j = 0
    count = 0
    for i in range(len(p)):
        if(p[i] == pattern):
            #print(i, end=": ")
            #print(codons[i])
            count += 1
        else:
            if(count>=threshold):
                res[str(j)] = count

            count = 0
            j = i+1
    print(res)

#test
records	= list(SeqIO.parse("sample_data/sample.fasta", "fasta"))
for dna in records:
    dna_seq = dna.seq
    repeats("CG", 2)
