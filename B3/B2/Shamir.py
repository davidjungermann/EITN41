from scipy import interpolate

def main():
    n = 8 #(input("Input the number of participants: "))
    t = 5 #int(input('Input the thresholdvalue: '))
    your_index = 1 #int(input("Input your participation number: "))
    
    incoming_shares = [75, 75, 54, 52, 77, 54, 43]
    outgoing_shares = [161, 568, 1565, 3578, 7153, 12956, 21773]
    polynom = [13, 8 ,11 ,1 ,5]
    x_values = []
    y_values = []
    x_values.append(1)
    x_values.append(2)
    x_values.append(4)
    x_values.append(5)
    x_values.append(7)
    point1 = calculate_point(incoming_shares, polynom, your_index)
    y_values.append(point1)
    y_values.append(2782)
    y_values.append(30822)
    y_values.append(70960)
    y_values.append(256422)
    # for i in range(n):
    #     if i  + 1 !=your_index:
    #        outgoing_shares.append(int(input("Input the value of your polynome for participan " + str(i + 1) + ": ")))
    
    # for i in range(n):
    #     if i + 1 !=your_index:
    #        outgoing_shares.append(int(input("Input the recieved value from participan " + str(i + 1) + ": ")))
    
    # print("Your polynom inputs: ")
    # for i in range(t):
    #     polynom.append(int(input("Input the coefficient for x" + "^" + str(i) + ": ")))
    # x_values.append(your_index) 
    # y_values.append(calculate_point(outgoing_shares, polynom, your_index))


    # print("Your incoming points: ")
    # for i in range(t - 1):
    #     x_values.append(int(input("Input the index for the point: ")))
    #     y_values.append(int(input("input the value for that index: ")))

    result = interpolate.lagrange(x_values, y_values)
    print(result)

def calculate_point(outgoing_shares, polynom, your_index):
    point = sum(outgoing_shares)
    for i in range(len(polynom)):
        point = point + polynom[i] * (your_index ** i)
        print(str(polynom[i]) + " * " + str(your_index) + " ** " + str(i))

    return(point)
main()