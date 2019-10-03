#Kevin Nunez
#CS-327-1, Spring 2018

def translate(input_mRNA):

    mRNA_list = []

    i = 0
    m = 0
    n = 3
    while i < len(input_mRNA):
        mRNA_list.append(input_mRNA[m:n])
        i += 3
        m += 3
        n += 3

    i = 0
    peptide_chain = []
    while i < len(mRNA_list):
        s = codon_table(mRNA_list[i])
        peptide_chain.append(s)
        i += 1

    return("".join(peptide_chain))

def codon_table(codon_String):

    codon_chart = {
        "UUU": 'F', "UUC": 'F',
        "UUA": 'L', "UUG": 'L',
        "CUU": 'L', "CUC": 'L', "CUA": 'L', "CUG": 'L',
        "AUU": 'I', "AUC": 'I', "AUA": 'I',
        "AUG": 'M',
        "GUU": 'V', "GUC": 'V', "GUA": 'V', "GUG": 'V',
        "UCU": 'S', "UCC": 'S', "UCA": 'S', "UCG": 'S',
        "CCU": 'P', "CCC": 'P', "CCA": 'P', "CCG": 'P',
        "ACU": 'T', "ACC": 'T', "ACA": 'T', "ACG": 'T',
        "GCU": 'A', "GCC": 'A', "GCA": 'A', "GCG": 'A',
        "UAU": 'Y', "UAC": 'Y',
        "UAA": '*', "UAG": '*',
        "CAU": 'H', "CAC": 'H',
        "CAA": 'Q', "CAG": 'Q',
        "AAU": 'N', "AAC": 'N',
        "AAA": 'K', "AAG": 'K',
        "GAU": 'D', "GAC": 'D',
        "GAA": 'E', "GAG": 'E',
        "UGU": 'C', "UGC": 'C',
        "UGA": '*',
        "UGG": 'W',
        "CGU": 'R', "CGC": 'R', "CGA": 'R', "CGG": 'R',
        "AGU": 'S', "AGC": 'S',
        "AGA": 'R', "AGG": 'R',
        "GGU": 'G', "GGC": 'G', "GGA": 'G', "GGG": 'G',
    }  # Amino Acid chart

    return codon_chart[codon_String]

