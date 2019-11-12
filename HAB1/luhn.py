
def luhn():
    f = open('testin.txt', "r")
    lines = f.readlines()
    f.close

    for line in lines:
        line = line[::-1]
        validate_string(line.strip())


def string_digit_conversion(string):
    return [int(digit) for digit in str(string)]


def unknown_removal(card_number):
    result = ''.join([i for i in card_number if i.isdigit()])
    return result


def validate_string(card_number):
    digits = unknown_removal(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    check = 0
    check += sum(string_digit_conversion(odd_digits))

    for digit in even_digits: 
        check += sum(string_digit_conversion(digit * 2)) 
    print(check % 10)
    return check % 10
    
    
    


luhn()
