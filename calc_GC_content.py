import Bio
from Bio import SeqIO
from Bio.SeqUtils import GC

records = list(SeqIO.parse("sample_data/ls_orchid.fasta", "fasta"))

for dna_rec in records[:10]:
    print(dna_rec.description)
    dna = dna_rec.seq[:100]
    print("GC Content: " + str(GC(dna)) + "%")
    print("")
