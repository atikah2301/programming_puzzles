# search algorithms
# number guessing game
import random as rand


def user_guess(num, lower, upper):
    print(f"Guess the number between {lower} and {upper} inclusive")
    i = 1
    while True:
        guess = int(input("Guess: "))
        if guess == num:
            break
        elif guess < num:
            print("Too low")
        elif guess > num:
            print("Too high")
        i += 1
    print(f"{guess} is correct. {i} guesses made.")


# def linear_search(num, lower, upper):
#     i = 1
#     print(f"Guessing between {lower} and {upper}")
#     while True:
#         guess = lower
#         if guess == num:
#             break
#         print(f"{guess} is too low.")
#         lower += 1
#         i += 1
#     print(f"{guess} is correct. {i} guesses made.")

def linear_search(num, lower, upper):
    print(f"Guessing between {lower} and {upper}")
    for i in range(lower, upper + 1):
        if i == num:
            print(f"{i} is correct. {i + 1 - lower} guesses made.")
            break
        print(f"{i} is incorrect")


# only works because the range of values is sorted
def binary_search(num, lower, upper):
    i = 1
    print(f"Guessing between {lower} and {upper}")
    while True:
        guess = (upper + lower) // 2
        print(guess)
        if guess == num:
            break
        elif guess < num:
            print("Too low")
            lower = guess
        elif guess > num:
            print("Too high")
            upper = guess
        i += 1
    print(f"{guess} is correct. {i} guesses made.")


def recursive_binary_search(num, lower, upper, count=1):
    guess = (upper + lower) // 2
    if guess == num:
        print(f"{guess} is correct. {count} guesses made.")
    elif guess < num:
        print(f"{guess} is too low")
        recursive_binary_search(num, guess, upper, count + 1)
    elif guess > num:
        print(f"{guess} is too high")
        recursive_binary_search(num, lower, guess, count + 1)


def random_search(num, lower, upper):
    i = 1
    fails = []
    print(f"Guessing between {lower} and {upper}")
    while True:
        guess = rand.randint(lower, upper)
        if guess in fails:
            continue
        if guess == num:
            break
        elif guess != num:
            print(f"{guess} is wrong")
            fails.append(guess)
        i += 1
    print(f"{guess} is correct. {i} guesses made.")


def test_func():
    """
    testing the use of enclosed variables as local variables
    """
    i = 0
    for i in range(20, 31):
        if i == 25:
            break
    print(i)


# random_search(4,0,10)
# linear_search(23, 20, 30)
recursive_binary_search(82, 1, 100)
#test_func()
