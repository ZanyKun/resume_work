

def integer_masses(acid):
    masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113,
              'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147,
              'R': 156, 'Y': 163, 'W': 186}
    return masses[acid]


def accumulating_sums(i, peptide, spectrum, sum):
    for j in range(i + 1, len(peptide)):
        sum += integer_masses(peptide[j])
        spectrum.append(sum)
    return spectrum, sum


def wrapping_sums(i, peptide, spectrum, sum):
    if i >= 2:
        for k in range(0, i - 1):
            sum += integer_masses(peptide[k])
            spectrum.append(sum)
    return spectrum


def linear_spectrum(peptide):
    spectrum = [0]
    for i in range(len(peptide)):
        sum = integer_masses(peptide[i])
        spectrum.append(sum)
        spectrum, sum = accumulating_sums(i, peptide, spectrum, sum)
    return sorted(spectrum)


def cyclic_spectrum(peptide):
    spectrum = [0]
    for i in range(len(peptide)):
        sum = integer_masses(peptide[i])
        spectrum.append(sum)
        spectrum, sum = accumulating_sums(i, peptide, spectrum, sum)
        spectrum = wrapping_sums(i, peptide, spectrum, sum)
    return sorted(spectrum)


def read_input(file_name):
    f = open(file_name, 'r')
    peptide = f.readline().rstrip('\n')
    ans_str = f.readline().rstrip('\n').split(' ')
    ans = [int(i) for i in ans_str]
    return peptide, ans


def check_answers(val, ans):
    if val == ans:
        print('Correct')
    else:
        print('Wrong')
    print(val)


def run_linear_spectrum(file_name):
    peptide, ans = read_input(file_name)
    val = linear_spectrum(peptide)
    check_answers(val, ans)


def run_cylic_spectrum(file_name):
    peptide, ans = read_input(file_name)
    val = cyclic_spectrum(peptide)
    check_answers(val, ans)


if __name__ == '__main__':
    run_linear_spectrum('P1a_short.txt')
    print()
    run_linear_spectrum('P1a_long.txt')
    print()
    run_cylic_spectrum('P1b_short.txt')
    print()
    run_cylic_spectrum('P1b_long.txt')