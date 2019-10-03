#Kevin Nunez
#CS-327-1, Spring 2018

def wrapping_sums(i, peptide, spectrum, sum):
    if i >= 2:
        for k in range(0, i - 1):
            sum += int(peptide[k])
            spectrum.append(sum)
    return spectrum

def accumulating_sums(i, peptide, spectrum, sum):
    for j in range(i + 1, len(peptide)):
        sum += int(peptide[j])
        spectrum.append(sum)
    return spectrum, sum

def cyclic_spectrum(peptide):
    spectrum = [0]
    for i in range(len(peptide)):
        sum = int(peptide[i])
        spectrum.append(sum)
        spectrum, sum = accumulating_sums(i, peptide, spectrum, sum)
        spectrum = wrapping_sums(i, peptide, spectrum, sum)
    return sorted(spectrum)

def read_input(filename):
    g = open(filename, 'r')
    peptide = g.readline().rstrip('\n').split('-')
    ans_str = g.readline().rstrip('\n').split(' ')
    ans = [int(i) for i in ans_str]
    g.close()
    return peptide, ans

def checking_answer(ans, user):
    if(ans == user):
        print("Correct")
    else:
        print("Wrong")
    print(user)

def run_cyclic_spectrum(filename):
    peptide, ans = read_input(filename)
    user = cyclic_spectrum(peptide)
    checking_answer(ans, user)

if __name__ == '__main__':
    run_cyclic_spectrum('cyclic_short.txt')
    print()
    run_cyclic_spectrum('cyclic_long.txt')