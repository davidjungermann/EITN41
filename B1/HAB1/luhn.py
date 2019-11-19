def main():
    lines = read_cards()
    for line in lines:
        digit_calc(line)


def digit_calc(number):
    number = reverse_number(number)
    x_index = index_of_x(number)
    calc_mod = (sum_calculation(number) % 10)

    value = (10 - calc_mod) % 10
    if (x_index) % 2 != 0:
        if value % 2 != 0:
            value += 9
        value /= 2
    print(str(int(value)), end="")
    return str(int(value))


def read_cards():
    f = open('test.txt', "r")
    lines = f.readlines()
    f.close
    return lines


def sum_calculation(number):
    sum = 0
    number = number.replace("X", "0")
    number = list(map(int, number))

    for i in range(len(number)):
        digit = number[i]
        if(i) % 2 != 0:
            digit *= 2
            if digit >= 10:
                digit = sum_digits(digit)
        sum += digit
    return sum


def index_of_x(number):
    return number.find("X")


def reverse_number(number):
    number = number.strip()
    number = number[::-1]
    return number

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

main()

