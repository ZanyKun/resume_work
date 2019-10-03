#Kevin Nunez
#CS-327-1, Spring 2018

import numpy as np
from backtrack import backtrack_matrix

def find_lcs(backing_m, v, w):
    lcs = ""
    i = len(v)
    j = len(w)

    while i != 0 and j != 0:
        if backing_m[i, j] == -1: #Down
            i -= 1
        elif backing_m[i, j] == 1: #Right
            j -= 1
        elif backing_m[i, j] == 0: #Diagonal
            lcs += v[i - 1]
            i -= 1
            j -= 1

    reverse_lcs = lcs[::-1]
    return reverse_lcs

def find_lcs_alignment(backing_m, v, w):
    i = len(v)
    j = len(w)

    v_sub = ""
    w_sub = ""

    while i != 0 and j != 0:
        if backing_m[i, j] == -1:#Down
            w_sub += "-"
            v_sub += v[i - 1]
            i -= 1
        elif backing_m[i, j] == 1:#Right
            v_sub += "-"
            w_sub += w[j - 1]
            j -= 1
        elif backing_m[i, j] == 0:#Diagonal
            v_sub += v[i - 1]
            w_sub += w[j - 1]
            i -= 1
            j -= 1

    v_sub = v_sub[::-1]
    w_sub = w_sub[::-1]

    return v_sub, w_sub

def read_input_lcs(filename):
    g = open(filename, 'r')
    v = list(g.readline().rstrip('\n'))
    w = list(g.readline().rstrip('\n'))
    ans = g.readline().rstrip('\n')

    backing_matrix = backtrack_matrix(v, w)

    return v, w, ans, backing_matrix

def read_input_lcs_alignment(filename):
    g = open(filename, 'r')
    v = list(g.readline().rstrip('\n'))
    w = list(g.readline().rstrip('\n'))
    v_ans = g.readline().rstrip('\n')
    w_ans = g.readline().rstrip('\n')

    backing_m = backtrack_matrix(v, w)

    return v, w, v_ans, w_ans, backing_m

def checking_lcs(user, given):
    if user == given:
        print("Correct LCS")
    else:
        print("Incorrect LCS")
    print(user)
    print(given)

def checking_lcs_alignment(v_sub, v_ans, w_sub, w_ans):
    if v_sub == v_ans:
        print("Correct V_Sub")
    else:
        print("Incorrect V_Sub")
    print(v_sub)
    print(v_ans)
    print()
    if w_sub == w_ans:
        print("Correct W_Sub")
    else:
        print("Incorrect W_Sub")
    print(w_sub)
    print(w_ans)

def run_lcs_algorithm(filename):
    v, w, ans, backing_matrix = read_input_lcs(filename)
    user = find_lcs(backing_matrix, v, w)
    checking_lcs(user, ans)

def run_lcs_alignment(filename):
    v, w, v_ans, w_ans, backing_m = read_input_lcs_alignment(filename)
    v_sub, w_sub = find_lcs_alignment(backing_m, v, w)
    checking_lcs_alignment(v_sub, v_ans, w_sub, w_ans)

if __name__ == '__main__':
    run_lcs_algorithm("P2a_short.txt")
    print()
    run_lcs_algorithm("P2a_long.txt")
    print()
    run_lcs_alignment("P2b_short.txt")
    print()
    run_lcs_alignment("P2b_long.txt")

