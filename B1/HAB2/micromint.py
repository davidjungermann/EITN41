# How many iterations (how many balls thrown) does it take before you generate c = 1, 100 and 10,000?

import random as random
import numpy as numpy
import math as math

c = int(input("Input the provided c: "))
u = int(input("Input the provided u: "))
k = int(input("Input the provided k: "))
interval_width = int(input("Input the provided confidence interval width: "))
lambda_value = 3.66

iteration_values = []
interval = interval_width + 1


def get_exp():
    return 2 ** int(u)


def create_bins():
    return [0] * get_exp()


def calc_conf_int():
    h = lambda_value * (numpy.std(iteration_values) /
                        math.sqrt(len(iteration_values)))
                        
    new_interval = (numpy.mean(iteration_values) + h) - \
        (numpy.mean(iteration_values) - h)

    if new_interval == 0:
        new_interval = interval

    return int(new_interval)


def generate_coins():
    nbr_of_coins = 0
    bins = create_bins()

    i = 0
    while True:
        random_index = random.randint(0, len(bins)-1)
        bins[random_index] += 1

        if bins[random_index] == k:
            nbr_of_coins += 1
            if nbr_of_coins == c:
                iteration_values.append(i)
                break
        i += 1


def main(interval):
    while interval > interval_width:
        generate_coins()
        interval = calc_conf_int()
        #print("Working...")
    print(numpy.mean(iteration_values))


main(interval)
