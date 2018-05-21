import Bio
from Bio import SeqIO
from Bio.Seq import Seq

records = list(SeqIO.parse("sample_data/ls_orchid.fasta", "fasta"))

for dna_rec in records[:10]:
    print(dna_rec.name)
    print(dna_rec.description)
    dna = dna_rec.seq[:90]
    print("DNA Sequence: "+dna)
    print("Reverse Complement: " + dna.reverse_complement())
    #Transcribing DNA to RNA
    print("RNA: " + dna.transcribe())
    #Transcribing RNA to Protein
    print("Protein: " + dna.translate())
    print("")
