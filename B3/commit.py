import hashlib
from random import randint


def create_commit(v, k, X):
    sha1 = hashlib.sha1()
    m = (bin(v)[2:] + k).encode()
    sha1.update(m)
    # Since we lose two bits after removing "0b" from bit strings.
    return sha1.hexdigest()[2: X + 2]


# Generate 16-bit random string as k.
def create_k(length):
    k = ''
    for i in range(length):
        k += str(randint(0, 1))
    return k

# Code from https://www.geeksforgeeks.org/python-intersection-two-lists/
def intersection(left, right):
    lst3 = [value for value in left if value in right]
    print(len(lst3))
    return len(lst3)


def construct_left_column(X):
    left_column = []

    for i in range(2**15, 2**16): 
        left_column.append(create_commit(0, create_k(16), X))
    return left_column


def construct_right_column(X):
    right_column = []

    for i in range(2**15, 2**16):
        right_column.append(create_commit(1, create_k(16), X))
    return right_column


def find_intersections(X):
    intersections_left = []
    intersections_right = []

    left_column = construct_left_column(X)
    right_column = construct_right_column(X)

    for i in range(1, X):
        for left, right in zip(left_column, right_column):
            intersections_left.append(left)
            intersections_right.append(right)
            print("Hej")
        print("Nbr of intersections found: " +
          str(intersection(intersections_left, intersections_right)))
        
find_intersections(10)
