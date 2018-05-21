import Bio
from Bio import SeqIO

records	= list(SeqIO.parse("sample_data/ls_orchid.gbk",	"genbank"))

for dna in records[:5]:
    print(dna.id)
    print(dna.name)
    print(dna.description)
    print(dna.seq[:100])

    #Display Annotations -
    for ann in dna.annotations.keys():
        print(ann, end=": ")
        print(dna.annotations[ann])
    print("")

    #Display features -
    for feature in dna.features:
        for q in feature.qualifiers:
            print(feature.type, end=" - ")
            print(q, end=": ")
            print(feature.qualifiers[q][0])

    #Display references -
    print("\nReferences -")
    for ref in dna.annotations['references']:
        print(ref)
    print("\n*********************************************************************\n")
