
def luhn():
    f = open('testin.txt', "r")
    lines = f.readlines()
    f.close

    for line in lines:
        line = line[::-1]
        print(line)

luhn()

