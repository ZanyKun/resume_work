#Kevin Nunez
#CS-327-1, Spring 2018

import numpy as np

def mtp(rows, columns, vertical_edge, horizon_edge):
    empty_matrix = np.zeros((rows, columns))

    for i in range(1, columns):
        empty_matrix[0, i] = empty_matrix[0, i - 1] + horizon_edge[0, i - 1]

    for i in range(1, rows):
        empty_matrix[i, 0] = empty_matrix[i - 1, 0] + vertical_edge[i - 1, 0]

    for i in range(1, columns):
        for j in range(1, rows):
            going_down = empty_matrix[i, j - 1] + horizon_edge[i, j - 1]
            going_right = empty_matrix[i - 1, j] + vertical_edge[i - 1, j]
            empty_matrix[i, j] = max(going_down, going_right)

    user_score = empty_matrix[rows - 1, columns - 1]
    return int(user_score)

def read_input(filename):
    g = open(filename, 'r')
    n_by_m = g.readline().rstrip('\n').split(' ')
    rows = int(n_by_m[0])
    columns = int(n_by_m[1])

    vertical_edge = getting_vertical_edges(g, rows)
    dash = g.readline().rstrip('\n')
    horizon_edge = getting_horizontal_edges(g, rows)
    correct_score = int(g.readline().rstrip('\n'))

    return rows, columns, vertical_edge, horizon_edge, correct_score

def getting_horizontal_edges(g, rows):
    horizon_matrix = []
    for i in range(0, rows):
        read = g.readline().rstrip('\n').split(' ')
        read_int = [int(i) for i in read]
        horizon_matrix.append(read_int)
    horizon_edge = np.array(horizon_matrix)
    return horizon_edge

def getting_vertical_edges(g, rows):
    vertical_matrix = []
    for i in range(0, rows - 1):
        read = g.readline().rstrip('\n').split(' ')
        read_int = [int(i) for i in read]
        vertical_matrix.append(read_int)
    vertical_edge = np.array(vertical_matrix)
    return vertical_edge


def checking_answer(user_score, correct_score):
    if user_score == correct_score:
        print("Correct Value")
    else:
        print("Incorrect Value")
    print(user_score)

def run_manhattan_tourist(filename):
    rows, columns, vertical_edge, horizon_edge, correct_score = read_input(filename)
    user_score = mtp(rows, columns, vertical_edge, horizon_edge)
    checking_answer(user_score, correct_score)

if __name__ == '__main__':
    run_manhattan_tourist("P2_short.txt")
    print()
    #run_manhattan_tourist("P2_long.txt")