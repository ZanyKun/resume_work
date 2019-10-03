# Kevin Nunez
# CS-327-1, Spring 2018

from spectral_convolution import convolution
from scoring import scoring
from spectrum import cyclic_spectrum
import collections
import heapq


def get_top_N_scores(pept_counts, n_value):
    key_list = pept_counts.keys()
    n_largest = heapq.nlargest(n_value, key_list)

    return n_largest


def get_top_scorers(pept_counts, top_n_scores, n_value):
    top_scorers = []

    i = 0
    while len(top_scorers) < n_value and i < len(top_n_scores):
        top_scorers.extend(pept_counts[top_n_scores[i]])
        i += 1

    return top_scorers


def branch(building_blocks, candidates):
    new_peptides = []

    for i in candidates:
        for j in building_blocks:
            new_peptides.append(str(i) + '-' + str(j))

    return new_peptides


def leaderboard(m_value, n_value, exp_spectrum):
    building_blocks = sorted(convolution(m_value, exp_spectrum))  # List of Integers
    candidates = list(building_blocks)  # Copy of Building_Blocks
    max_exp = max(building_blocks)
    leader = '0'  # String

    while candidates:
        d = collections.defaultdict(list)
        candidates = branch(building_blocks, candidates)  # List of Strings (Str-Str)
        candidate_copy = list(candidates)
        for peptide in candidate_copy:
            testing_peptide = peptide
            split_peptide = testing_peptide.split('-')
            candidate_cyclic_spec = cyclic_spectrum(split_peptide)  # Returns a list of integers
            max_theo = max(candidate_cyclic_spec)
            if max_theo > max_exp:
                candidate_copy.remove(testing_peptide)
            else:
                theo_score = scoring(candidate_cyclic_spec, exp_spectrum)
                leader_peptide = leader.split('-')
                leader_cyclic_spec = cyclic_spectrum(leader_peptide)  # Returns a list of integers
                leader_score = scoring(leader_cyclic_spec, exp_spectrum)
                if theo_score > leader_score:
                    leader = testing_peptide
                d[theo_score].append(testing_peptide)

            top_n_scores = get_top_N_scores(d, n_value)
            candidates = get_top_scorers(d, top_n_scores, n_value)

    return leader


def read_input(filename):
    g = open(filename, 'r')
    m_value = int(g.readline().rstrip('\n'))
    n_value = int(g.readline().rstrip('\n'))
    read_exp_spectrum = g.readline().rstrip('\n').split(' ')
    exp_spectrum = [int(i) for i in read_exp_spectrum]
    ans = g.readline().rstrip('\n')
    return m_value, n_value, exp_spectrum, ans


def checking_answer(user, ans):
    if (user == ans):
        print("Correct")
    else:
        print("Incorrect")
    print(user)
    print(ans)


def run_leaderboard_algorithm(filename):
    m_value, n_value, exp_spectrum, ans = read_input(filename)
    user = leaderboard(m_value, n_value, exp_spectrum)
    checking_answer(user, ans)


if __name__ == '__main__':
    run_leaderboard_algorithm("P2_short.txt")
    print()
    run_leaderboard_algorithm("P2_long.txt")
