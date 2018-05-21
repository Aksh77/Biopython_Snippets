amino_codon = {     'Alanine': ['GCU', 'GCC', 'GCA', 'GCG'],
                    'Arginine': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
                    'Asparagine': ['AAU', 'AAC'],
                    'Aspartic acid': ['GAU', 'GAC'],
                    'Cysteine': ['UGU', 'UGC'],
                    'Glutamic acid': ['GAA', 'GAG'],
                    'Glutamine': ['CAA', 'CAG'],
                    'Glycine': ['GGU', 'GGC', 'GGA', 'GGG'],
                    'Histidine': ['CAU', 'CAC'],
                    'Isoleucine': ['AUU', 'AUC', 'AUA'],
                    'Leucine': ['CUU', 'CUC', 'CUA', 'CUG', 'UUA', 'UUG'],
                    'Lysine': ['AAA', 'AAG'],
                    'Methionine': ['AUG'],
                    'Phenylalanine': ['UUU', 'UUC'],
                    'Proline': ['CCU', 'CCC', 'CCA', 'CCG'],
                    'Serine': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
                    'Stop': ['UAA', 'UAG', 'UGA'],
                    'Threonine': ['ACU', 'ACC', 'ACA', 'ACG'],
                    'Tryptophan': ['UGG'],
                    'Tyrosine': ['UAU', 'UAC'],
                    'Valine': ['GUU', 'GUC', 'GUA', 'GUG']
              }

codon_amino = { 'AAC': 'N', 'UCC': 'S', 'GUG': 'V', 'AUA': 'I', 'UAA': '*', 'CGG': 'R', 'AUC': 'I', 'GCU': 'A', 'ACG': 'T', 'CGA': 'R', 
                'UGG': 'W', 'CCG': 'P', 'GUU': 'V', 'UUA': 'L', 'CCU': 'P', 'UAU': 'Y', 'CGU': 'R', 'GCC': 'A', 'ACA': 'T', 'GAA': 'E', 
                'CAC': 'H', 'UUG': 'L', 'AGG': 'R', 'CGC': 'R', 'UCA': 'S', 'UCG': 'S', 'CCA': 'P', 'UGU': 'C', 'AAU': 'N', 'GCG': 'A', 
                'GGA': 'G', 'AUU': 'I', 'UAG': '*', 'ACC': 'T', 'UUU': 'F', 'UGC': 'C', 'GUC': 'V', 'UGA': '*', 'AGA': 'R', 'CAU': 'H', 
                'GUA': 'V', 'CCC': 'P', 'CUG': 'L', 'GGC': 'G', 'CUC': 'L', 'GAU': 'D', 'GGG': 'G', 'AGC': 'S', 'UCU': 'S', 'ACU': 'T', 
                'CAG': 'Q', 'GAG': 'E', 'UAC': 'Y', 'GCA': 'A', 'AUG': 'M', 'GAC': 'D', 'CUU': 'L', 'AAA': 'K', 'CUA': 'L', 'AGU': 'S', 
                'UUC': 'F', 'AAG': 'K', 'GGU': 'G', 'CAA': 'Q'}