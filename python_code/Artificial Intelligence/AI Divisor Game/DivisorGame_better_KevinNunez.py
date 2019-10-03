# Kevin Nunez
# CS-335, Spring 2019
# Asst 6

import math


def number_factors(n):
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list


def result(current_state, action):
    factors_left = list(current_state)
    for i in range(1, action + 1):
        if action % i == 0 and i in factors_left:
            factors_left.remove(i)
    return factors_left


def DG_betterMinValue(s):
    v = math.inf
    for a in s:
        temp = DG_betterMaxValue(result(s, a))
        if temp < v:
            v = temp
            if v == -1:
                return v
    return v


def DG_betterMaxValue(s):
    v = -math.inf
    for a in s:
        temp = DG_betterMinValue(result(s, a))
        if temp > v:
            v = temp
            if v == 1:
                return v
    return v


def DG_betterMaxValue_Action(s, turn):
    if len(s) == 1:
        return s[0]
    if turn == 2:
        v = DG_betterMaxValue(s)
        best_action = 0
        for a in s:
            temp = DG_betterMaxValue(result(s, a))
            if temp == v:
                best_action = a
        return best_action
    if turn == 1:
        v = DG_betterMinValue(s)
        best_action = 0
        for a in s:
            temp = DG_betterMinValue(result(s, a))
            if temp == v:
                best_action = a
        return best_action


def divisor_game(name, turn, factors):
    human_win = True
    ai_win = True
    current_factors = factors

    while human_win and ai_win:
        if turn == 1:
            print("Here are the remaining numbers: " + str(current_factors))
            choice_human = int(input(name + ", pick a number from the list above: "))
            while choice_human not in current_factors:
                choice_human = int(input("Enter a number from the list above: "))
            if choice_human == n:
                human_win = False
                break
            else:
                current_factors = result(current_factors, choice_human)
            print()
            print("Here are the remaining numbers: " + str(current_factors))
            choice_ai = DG_betterMaxValue_Action(current_factors, 2)
            print("My pick is " + str(choice_ai))
            if choice_ai == n:
                ai_win = False
                break
            else:
                current_factors = result(current_factors, choice_ai)
            print()
        if turn == 2:
            print("Here are the remaining numbers: " + str(current_factors))
            choice_ai = DG_betterMaxValue_Action(current_factors, 1)
            print("My pick is " + str(choice_ai))
            print()
            if choice_ai == n:
                ai_win = False
                break
            else:
                current_factors = result(current_factors, choice_ai)
            print("Here are the remaining numbers: " + str(current_factors))
            choice_human = int(input(name + ", pick a number from the list above: "))
            while choice_human not in current_factors:
                choice_human = int(input("Enter a number from the list above: "))
            if choice_human == n:
                human_win = False
                break
            else:
                current_factors = result(current_factors, choice_human)
            print()

    print()
    if human_win:
        print("It's your victory, " + name + "!\nYou Win!")
    elif ai_win:
        print("Seems the A.I won, " + name + "...\nYou Lose.")


if __name__ == "__main__":
    name = input("Enter your name: ")
    turn = int(input("Enter 1 to go first, 2 to go second: "))
    print()
    n = int(input("Enter a positive integer n: "))
    print()
    factors = number_factors(n)
    divisor_game(name, turn, factors)