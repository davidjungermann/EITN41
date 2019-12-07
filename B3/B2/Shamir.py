from scipy import interpolate


def calculate_point(outgoing_shares, polynom, your_index):
    point = sum(outgoing_shares)
    for i in range(len(polynom)):
        point = point + polynom[i] * (your_index ** i)
        print(str(polynom[i]) + " * " + str(your_index) + " ** " + str(i))
    return(point)

def main():
    your_index = 1
    k = 3
    n = 6 

    polynome = [9, 19, 5]
    outgoing_shares = [67, 111, 165, 229, 303]
    incoming_shares = [37, 18, 40, 44, 28]
    x_values = [your_index, 4, 5]
    point1 = calculate_point(incoming_shares, polynome, your_index)
    y_values = [point1, 1385, 2028]

    result = interpolate.lagrange(x_values, y_values)
    print(result)
    print(int(result(0)))

main()
