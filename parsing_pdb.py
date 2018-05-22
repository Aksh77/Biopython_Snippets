from Bio import PDB
parser = PDB.PDBParser()
struc =	parser.get_structure("rna", "sample_data/asptrna.pdb")
n_atoms	= 0
for	model in struc:
    for	chain in model:
        for	residue	in chain:
                for	atom in	residue:
                    print(residue.resname,	residue.id)
                n_atoms	+=	1
print(n_atoms)
