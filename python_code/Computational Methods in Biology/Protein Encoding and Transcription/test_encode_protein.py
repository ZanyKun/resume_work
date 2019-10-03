#Kevin Nunez
#CS-327-1, Spring 2018

from encode_protein import translate


def test_protein_check(input, output):
    protein = translate(input)
    if protein == output:
        print('Test passed.')
        print('Protein: ' + protein)
    else:
        print('Test failed.')
        print('Incorrect protein: ' + protein)


def run_tests():
    f = open('shortRNA.txt', 'r')
    input_mRNA1 = f.readline().rstrip('\n')
    input_protein1 = f.readline().rstrip('\n')
    test_protein_check(input_mRNA1, input_protein1)
    f.close()
    print()
    g = open("longRNA.txt", 'r')
    input_mRNA2 = g.readline().rstrip('\n')
    input_protein2 = g.readline().rstrip('\n')
    test_protein_check(input_mRNA2, input_protein2)
    g.close()


def main():
    run_tests()


if __name__ == "__main__":
    main()