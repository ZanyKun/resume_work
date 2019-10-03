#Kevin Nunez
#CS-327-1, Spring 2018

from transcribe import dna_to_rna


def test_dna_to_rna(input, output):
    rna = dna_to_rna(input)
    if rna == output:
        print('Test passed.')
        print('mRNA: ' + rna)
    else:
        print('Test failed.')
        print('Incorrect mRNA: ' + rna)


def run_tests():
    f = open('dna.txt')
    dna1 = f.readline().rstrip('\n')
    rna1 = f.readline().rstrip('\n')
    test_dna_to_rna(dna1, rna1)
    print()
    dna2 = f.readline().rstrip('\n')
    rna2 = f.readline().rstrip('\n')
    test_dna_to_rna(dna2, rna2)


def main():
    run_tests()


if __name__ == "__main__":
    main()