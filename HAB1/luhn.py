
def luhn():
    f = open('test.txt', "r")
    lines = f.readlines()
    f.close

    for line in lines:
        line = line.strip()
        reversed_lines = line[::-1]
        odd_index = reversed_lines[1::2]
        even_index = reversed_lines[::2]

        odd_index = odd_index.replace("X", "0")
        even_index = even_index.replace("X", "0")

        odd_index = list(map(int, odd_index))
        even_index = list(map(int, even_index))  

        odd_sum = sum(odd_index)  

        even_index = [x * 2 for x in even_index]

        digit_sum = 0
        for number in even_index:
            digit_sum += sum(map(int, str(number)))
        
        result = (10 - ((digit_sum + odd_sum) % 10))
        print(result)
        
luhn()

