from textwrap import wrap


def luhn():
    f = open('testin.txt', "r")
    lines = f.readlines()
    f.close

    for line in lines:
        line = line[::-1]
        line = line.strip()
        chars = letter_slice(line, 2)
                
def letter_slice(string, index):
    return string[::index]


luhn()
