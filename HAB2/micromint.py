# How many iterations (how many balls thrown) does it take before you generate c = 1, 100 and 10,000?

import random

c = int(input("Input the provided c: "))
u = int(input("Input the provided u: "))
k = int(input("Input the provided k: "))
interval_width = int(input("Input the provided confidence interval width: "))
lambda_value = 3.66


def get_exp():
    return 2 ** int(u)


def create_bins():
    return [0] * get_exp()


def generate_coins():
    nbr_of_coins = 0
    bins = create_bins()

    while True:
        bins[random.randint(0, get_exp())] += 1

        if any(balls > k for balls in bins):
            nbr_of_coins += 1
            if nbr_of_coins > c:
                print(bins)
                break


generate_coins()
