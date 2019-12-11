from scipy import interpolate


def calculate_point(outgoing_shares, polynom, your_index):
    point = sum(outgoing_shares)
    for i in range(len(polynom)):
        point = point + polynom[i] * (your_index ** i)
        print(str(polynom[i]) + " * " + str(your_index) + " ** " + str(i))
    return(point)


def main():
    your_index = 1
    k = 4
    n = 6

    polynome = [14, 11, 16, 12]
    outgoing_shares = [196, 515, 1082, 1969, 3248]  # Not used
    incoming_shares = [27, 51, 26, 45, 42]
    x_values = [your_index, 4, 5, 6]
    point1 = calculate_point(incoming_shares, polynome, your_index)
    y_values = [point1, 5815, 10792, 18049]

    result = interpolate.lagrange(x_values, y_values)
    print(result)
    print(int(result(0)))

main()
