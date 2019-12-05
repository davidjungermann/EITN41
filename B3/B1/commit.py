import hashlib
import matplotlib.pyplot
from random import randint

x_values = []
y_values = []

# Generates a commit according to the commitment scheme.
# Returns a bit version of a hashed string.


def create_commit(v, k):
    m = str(bin(v)[2:] + bin(k)[2:])
    hash_object = hashlib.sha1(m.encode())
    hash_value = hash_object.hexdigest()
    return bin(int(hash_value, 16))

# Generates a list of all possible k values to break binding.
# Task suggests a random string, but also suggests a "non-idiot" attacker?


def create_k():
    values_of_k = []
    for i in range(0, 2 ** 16 - 1):
        values_of_k.append(i)
    return values_of_k

# Constructs a dictionary with all possible commit-values for v = 0 and v = 1.


def construct_columns(values, X):
    left_column = []
    right_column = []

    for k in values:
        left_column.append(create_commit(0, k))
        right_column.append(create_commit(1, k))

    dict = {"left": left_column, "right": right_column}
    return dict


# Code from https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(left, right):
    commit_hit = 0
    non_commit_hit = 0
    res = [value for value in left if value in right]
    return res


def find_binding_collisions(X):

    columns = construct_columns(create_k(), X)
    left_column = columns.get("left")
    right_column = columns.get("right")

    for trunc_value in range(X):
        possible_intersections_left = []
        possible_intersections_right = []
        left_set = set()
        right_set = set()
        total_commits = 0

        for left in left_column:
            possible_intersections_left.append(left[2: trunc_value + 2])
            left_set.add(left[2: trunc_value + 2])
        for right in right_column:
            possible_intersections_right.append(right[2: trunc_value + 2])
            right_set.add(right[2: trunc_value + 2])
        res = intersection(
            possible_intersections_left, right_set)
        nbr_of_collisions = len(res)

        add_to_plot(trunc_value, nbr_of_collisions / len(columns))
        print("Nbr of collisions for X-value = " +
              str(trunc_value) + " : " + str(nbr_of_collisions))

    binding_stats(x_values, y_values)

def add_to_plot(x, y):
    x_values.append(x)
    y_values.append(y)


def binding_stats(x, y):
    stats = matplotlib.pyplot
    stats.plot(x, y)
    stats.xlabel("Hash output length")
    stats.ylabel("Collisions")
    stats.title("Number of collisions on varying SHA-1 output lengths")
    stats.show()


find_binding_collisions(35)
