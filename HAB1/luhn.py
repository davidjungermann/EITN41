from textwrap import wrap


def luhn():
    f = open('testin.txt', "r")
    lines = f.readlines()
    f.close

    for line in lines:
        line = line[::-1]
        validate_string(line.strip())
                
def letter_slice(string, index):
    return string[::index]

def validate_string(string):
    chars = letter_slice(string, 2)
    


luhn()
