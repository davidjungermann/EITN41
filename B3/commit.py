import hashlib
from random import randint


def create_commit(v, k, X):
    m = str(bin(v)[2:] + bin(k)[2:])
    hash_object = hashlib.sha1(m.encode())
    hash_value = hash_object.hexdigest()
    return hash_value[2: X + 2]


def create_k():
    values_of_k = []

    for i in range(1, 10):
        values_of_k.append(i)
    return values_of_k


def construct_left_column(values, X):
    left_column = []

    for k in values:
        left_column.append(create_commit(0, k, X))
    return left_column


def construct_right_column(values, X):
    right_column = []

    for k in values:
        right_column.append(create_commit(1, k, X))

    return right_column

# Code from https://www.geeksforgeeks.org/python-intersection-two-lists/


def intersection(left, right):
    res = [value for value in left if value in right]
    print(res)
    return len(res)


def find_intersections(X):

    left_column = construct_left_column(create_k(), X)
    right_column = construct_right_column(create_k(), X)

    for trunc_value in range(1, X):
        possible_intersections_left = []
        possible_intersections_right = []

        for left in left_column:
            possible_intersections_left.append(left)

        for right in right_column:
            possible_intersections_right.append(right)
        
        print("Nbr of intersections: " + str(intersection(possible_intersections_left,
                                                          possible_intersections_right)) + " for X-value = " + str(trunc_value))

find_intersections(10)
