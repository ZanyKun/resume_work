# Kevin Nunez
# CS-335, Spring 2019
# Asst 5


def number_factors(n):
    factor_list = []

    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)

    return factor_list


def remove_factors(choice, current_factors):
    factors_left = list(current_factors)
    for i in range(1, choice + 1):
        if choice % i == 0 and i in factors_left:
            factors_left.remove(i)

    return factors_left


def the_game(human, factors, n, turn):
    human_win = True
    computer_win = True
    current_factors = factors

    while human_win and computer_win:
        if turn == 1:
            print("Here are the remaining numbers: " + str(current_factors))
            choice_human = int(input(human + ", pick a number from the list above: "))
            if choice_human == n:
                human_win = False
                break
            else:
                current_factors = remove_factors(choice_human, current_factors)
            print()
            print("Here are the remaining numbers: " + str(current_factors))
            choice_computer = current_factors.pop(0)
            print("My pick is " + str(choice_computer))
            if choice_computer == n:
                second_win = False
                break
            else:
                current_factors = remove_factors(choice_computer, current_factors)
            print()
        if turn == 2:
            print("Here are the remaining numbers: " + str(current_factors))
            choice_computer = current_factors.pop(0)
            print("My pick is " + choice_computer)
            print()
            if choice_computer == n:
                second_win = False
                break
            else:
                current_factors = remove_factors(choice_computer, current_factors)
            print("Here are the remaining numbers: " + str(current_factors))
            choice_human = int(input(human + ", pick a number from the list above: "))
            if choice_human == n:
                human_win = False
                break
            else:
                current_factors = remove_factors(choice_human, current_factors)
            print()

    print()
    if not human_win:
        print("You lose " + human + "!\n")
        print("Bye!")
    elif not second_win:
        print("I lose!\n")
        print("Bye!")


if __name__ == "__main__":
    first = input("Enter your name: ")
    n = int(input("Enter a positive integer n: "))
    factors = number_factors(n)
    turn = int(input("Enter 1 if you want to go first, 2 for second: "))
    print()
    the_game(first, factors, n, turn)