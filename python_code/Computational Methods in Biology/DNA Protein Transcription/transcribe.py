#Kevin Nunez
#CS-327-1, Spring 2018

def dna_to_rna(input):

    rna_translate = list(input)

    for i in range(len(rna_translate)):
        if rna_translate[i] is 'A':
            rna_translate[i] = 'U'
        elif rna_translate[i] is 'T':
            rna_translate[i] = 'A'
        elif rna_translate[i] is 'G':
            rna_translate[i] = 'C'
        elif rna_translate[i] is 'C':
            rna_translate[i] = 'G'

    return ("".join(rna_translate))