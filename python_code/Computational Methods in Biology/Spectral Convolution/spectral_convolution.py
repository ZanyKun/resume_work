#Kevin Nunez
#CS-327-1, Spring 2018

from collections import Counter
import collections
import heapq

def convolution(m_value, exp_spec):
    difference_list = []

    for i in exp_spec:
        for j in exp_spec:
            difference = i - j
            if(57 <= difference <= 200):
                difference_list.append(difference)

    occur = Counter(difference_list)
    most_freqs = collections.defaultdict(list)

    for count, value in occur.items():
        most_freqs[value].append(count)
    m_occuring = heapq.nlargest(m_value, most_freqs.keys())

    return_list = []

    index = 0
    while len(return_list) < m_value:
        occurence = most_freqs[m_occuring[index]]
        for i in occurence:
            return_list.append(i)
        index += 1

    return return_list

def read_input(filename):
    g = open(filename, 'r')
    m_value = int(g.readline().rstrip('\n'))
    read_spec = g.readline().rstrip('\n').split(' ')
    exp_spec = [int(i) for i in read_spec]
    read_ans = g.readline().rstrip('\n').split(' ')
    ans = [int(i) for i in read_ans]

    return m_value, exp_spec, ans

def checking_answer(user_spectral, ans):
    user = sorted(user_spectral)
    answer = sorted(ans)
    if(user == answer):
        print("Correct")
    else:
        print("Incorrect")
    print(user)
    print(answer)

def run_special_convolution(filename):
    m_value, exp_spec, ans = read_input(filename)
    user_spectral = convolution(m_value, exp_spec)
    checking_answer(user_spectral, ans)

if __name__ == '__main__':
    run_special_convolution("P1_short.txt")
    print()
    run_special_convolution('P1_long.txt')