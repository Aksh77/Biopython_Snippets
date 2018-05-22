import Bio
from Bio import SeqIO

def triplets(string):
    return (string[0+i:3+i] for i in range(0, len(string), 3))

records	= list(SeqIO.parse("sample_data/ls_orchid.gbk", "genbank"))
for dna in records:
    dna_seq = dna.seq
    triplets_list = list(triplets(dna_seq))
    for triplet in triplets_list:
        print(triplet)
    print("**************")
