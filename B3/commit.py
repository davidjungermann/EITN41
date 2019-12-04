import hashlib
from random import randint


def create_commit(v, k, X):
    m = str(bin(v)[2:] + bin(k)[2:])
    hash_object = hashlib.sha1(m.encode())
    hash_value = hash_object.hexdigest()
    return hash_value


def create_k():
    values_of_k = []

    for i in range(1, 20):
        values_of_k.append(i)
    return values_of_k


def construct_columns(values, X):
    left_column = []
    right_column = []

    for k in values:
        left_column.append(create_commit(0, k, X))
        right_column.append(create_commit(1, k, X))

    dict = {"left": left_column, "right": right_column}
    return dict


# Code from https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(left, right):
    res = [value for value in left if value in right]
    return len(res)


def find_intersections(X):

    columns = construct_columns(create_k(), X)
    left_column = columns.get("left")
    right_column = columns.get("right")

    for trunc_value in range(1, X):
        possible_intersections_left = []
        possible_intersections_right = []

        for left in left_column:
            possible_intersections_left.append(left[2: trunc_value + 2])

        for right in right_column:
            possible_intersections_right.append(right[2: trunc_value + 2])

        print("Nbr of intersections for X-value = " + str(trunc_value) + " : " + str(intersection(possible_intersections_left,
                                                                                                  possible_intersections_right)))


find_intersections(35)
