#Kevin Nunez
#CS-327-1, Spring 2018

from Bio.SubsMat import MatrixInfo

def similarity(amino_one, amino_two):
    user_similar = 0

    bio_matrix = MatrixInfo.blosum50

    for i in range(0, len(amino_one)):
        if (amino_one[i], amino_two[i]) in bio_matrix:
            score = bio_matrix[amino_one[i], amino_two[i]]
        else:
            score = bio_matrix[amino_two[i], amino_one[i]]
        user_similar += score

    identical = 0
    residue = len(amino_one)

    for i in range(0, len(amino_one)):
        if amino_one[i] == amino_two[i]:
            identical += 1

    user_percent = (identical / residue) * 100

    return user_similar, user_percent

def read_input(filename):
    g = open(filename, 'r')
    amino_one = list(g.readline().rstrip('\n'))
    amino_two = list(g.readline().rstrip('\n'))
    similar = int(g.readline().rstrip('\n'))
    percent = float(g.readline().rstrip('\n'))
    return amino_one, amino_two, similar, percent

def checking_answers(user_similar, correct_sim, user_percent, correct_per):
    if user_similar == correct_sim:
        print("Correct Similarity")
    else:
        print("Incorrect Similarity")
    print(user_similar)
    if user_percent == correct_per:
        print("Correct Percent Similarity")
    else:
        print("Incorrect Percent Similarity")
    print(user_percent)

def run_similarities(filename):
    amino_one, amino_two, similar, percent = read_input(filename)
    user_similar, user_percent = similarity(amino_one, amino_two)
    checking_answers(user_similar, similar, user_percent, percent)

if __name__ == '__main__':
    run_similarities("P1_short.txt")
    print()
    run_similarities("P1_long.txt")