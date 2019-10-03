#Kevin Nunez
#CS-327-1, Spring 2018

from Bio.SubsMat import MatrixInfo
from subsequences import find_lcs_alignment
import numpy as np

def score_backtrack(v, w):
    score_matrix = np.zeros((len(v) + 1, len(w) + 1), dtype='int64')
    backtracking = np.zeros((len(v) + 1, len(w) + 1), dtype='int64')

    bio_matrix = MatrixInfo.blosum62

    for i in range(1, len(v) + 1): # Horizontal Edges
        score_matrix[i, 0] = score_matrix[i - 1, 0] - 5

    for j in range(1, len(w) + 1): # Vertical Edges
        score_matrix[0, j] = score_matrix[0, j - 1] - 5

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            going_down = score_matrix[i - 1, j] - 5
            going_right = score_matrix[i, j - 1] - 5
            if w[j - 1] == v[i - 1]:
                amino_one = w[j - 1]
                amino_two = v[i - 1]
                if (amino_one, amino_two) in bio_matrix:
                    going_diag = score_matrix[i - 1, j - 1] + bio_matrix[amino_one, amino_two]
                else:
                    going_diag = score_matrix[i - 1, j - 1] + bio_matrix[amino_two, amino_one]
            else:
                amino_one = w[j - 1]
                amino_two = v[i - 1]
                if (amino_one, amino_two) in bio_matrix:
                    going_diag = score_matrix[i - 1, j - 1] - bio_matrix[amino_one, amino_two]
                else:
                    going_diag = score_matrix[i - 1, j - 1] - bio_matrix[amino_two, amino_one]
            score_matrix[i, j] = max(going_down, going_right, going_diag)

            amino_one = w[j - 1]
            amino_two = v[i - 1]
            if (amino_one, amino_two) in bio_matrix:
                mu = bio_matrix[amino_one, amino_two]
            else:
                mu = bio_matrix[amino_two, amino_one]
            if score_matrix[i, j] == score_matrix[i - 1, j] - 5:  # Down
                backtracking[i, j] = -1
            elif score_matrix[i, j] == score_matrix[i, j - 1] - 5:  # Right
                backtracking[i, j] = 1
            elif score_matrix[i, j] == score_matrix[i - 1, j - 1] + mu and amino_one == amino_two:  # Diagonal
                backtracking[i, j] = 0

    user_score = score_matrix[len(v), len(w)]
    return user_score, backtracking

def read_input(filename):
    g = open(filename, 'r')
    v = list(g.readline().rstrip('\n'))
    w = list(g.readline().rstrip('\n'))
    correct_score = int(g.readline().rstrip('\n'))
    v_alignment = g.readline().rstrip('\n')
    w_alignment = g.readline().rstrip('\n')

    return v, w, correct_score, v_alignment, w_alignment

def checking_answers(user_score, user_backtrack_m, correct_score, v_alignment, w_alignment, v, w):
    if user_score == correct_score:
        print("Correct Score")
    else:
        print("Incorrect Score")
    print(user_score)
    print()
    v_sub, w_sub = find_lcs_alignment(user_backtrack_m, v, w)
    if v_sub == v_alignment:
        print("Correct v_sub")
    else:
        print("Incorrect v_sub")
    print("My v_sub:")
    print(v_sub)
    print("Correct v_sub:")
    print(v_alignment)
    if w_sub == w_alignment:
        print("Correct w_sub")
    else:
        print("Incorrect w_sub")
    print("My w_sub:")
    print(w_sub)
    print("Correct w_sub:")
    print(w_alignment)


def run_global_alignment(filename):
    v, w, correct_score, v_alignment, w_alignment = read_input(filename)
    user_score, user_backtrack_m = score_backtrack(v, w)
    checking_answers(user_score, user_backtrack_m, correct_score, v_alignment, w_alignment, v, w)

if __name__ == '__main__':
    run_global_alignment("P3_short.txt")
    print()
    run_global_alignment("P3_long.txt")