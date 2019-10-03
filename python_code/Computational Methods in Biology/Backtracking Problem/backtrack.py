#Kevin Nunez
#CS-327-1, Spring 2018

import numpy as np

def backtrack_matrix(v, w):
    score_matrix = np.zeros((len(v) + 1, len(w) + 1), dtype='int64')
    backtracking = np.zeros((len(v) + 1, len(w) + 1), dtype='int64')

    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            going_down = score_matrix[i - 1, j] + 0
            going_right = score_matrix[i, j - 1] + 0
            if w[j - 1] == v[i - 1]:
                going_diag = score_matrix[i - 1, j - 1] + 1
            else:
                going_diag = score_matrix[i - 1, j - 1] + 0
            score_matrix[i, j] = max(going_down, going_right, going_diag)

            if score_matrix[i, j] == score_matrix[i - 1, j]:
                backtracking[i, j] = -1
            elif score_matrix[i, j] == score_matrix[i, j - 1]:
                backtracking[i, j] = 1
            elif score_matrix[i, j] == score_matrix[i - 1, j - 1] and v[i - 1] == w[j - 1]:
                backtracking[i, j] = 0

    return backtracking

def read_input(filename):
    g = open(filename, 'r')
    v = list(g.readline().rstrip('\n'))
    w = list(g.readline().rstrip('\n'))

    backtrack = []
    for i in range(0, len(w)):
        read = g.readline().rstrip('\n').split(' ')
        read_int = [int(i) for i in read]
        backtrack.append(read_int)
    backtrack_m = np.array(backtrack)

    backtrack_m = np.asmatrix(backtrack_m)

    return v, w, backtrack_m

def checking_answer(user, given):
    if user.all() == given.all():
        print("Correct")
    else:
        print("Incorrect")
    print(user)

def run_backtrack(filename):
    v, w, backtrack_m = read_input(filename)
    user_backtrack = backtrack_matrix(v, w)
    checking_answer(user_backtrack, backtrack_m)

if __name__ == '__main__':
    run_backtrack("P1_short.txt")