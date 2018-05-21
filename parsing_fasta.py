import Bio
from Bio import SeqIO

records = list(SeqIO.parse("sample_data/ls_orchid.fasta", "fasta"))

for dna in records:
    print(dna.name)
    print(dna.description)
    print(dna.seq[:100])
    print("")
