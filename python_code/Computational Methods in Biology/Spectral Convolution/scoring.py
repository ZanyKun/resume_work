#Kevin Nunez
#CS-327-1, Spring 2018

import collections

def scoring(theo, exp):
    count_theo = collections.Counter()
    count_exp = collections.Counter()
    getting_counts(count_exp, count_theo, exp, theo)

    score = 0
    score = calculating_score(count_exp, count_theo, score)

    return score


def getting_counts(count_exp, count_theo, exp, theo):
    for i in theo:
        count_theo[i] += 1
    for i in exp:
        count_exp[i] += 1


def calculating_score(count_exp, count_theo, score):
    for amino_acid, occur in count_theo.items():
        if amino_acid in count_exp:
            theo_value = count_theo.get(amino_acid, occur)
            exp_value = count_exp.get(amino_acid, occur)
            if (theo_value < exp_value):
                score += theo_value
            else:
                score += exp_value
    return score


def read_input(filename):
    g = open(filename, 'r')
    theo = g.readline().rstrip('\n').split(' ')
    exp = g.readline().rstrip('\n').split(' ')
    ans = int(g.readline().rstrip('\n'))
    g.close()
    return theo, exp, ans

def checking_answers(user, ans):
    if(user == ans):
        print("Correct")
    else:
        print("Incorrect")
    print(user)

def run_scoring(filename):
    theo, exp, ans = read_input(filename)
    user = scoring(theo, exp)
    checking_answers(user, ans)

if __name__ == '__main__':
    run_scoring("score_short.txt")
    print()
    run_scoring("score_long.txt")