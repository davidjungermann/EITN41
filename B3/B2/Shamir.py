

def main():
    n = int(input("Input the number of participants: "))
    t = int(input('Input the thresholdvalue: '))
    your_index = int(input("Input your participation number: "))
    
    incoming_shares = []
    outgoing_shares = []
    polynom = []
    known_points = {}

    for i in range(n):
        if i  + 1 !=your_index:
           outgoing_shares.append(int(input("Input the value of your polynome for participan " + str(i + 1) + ": ")))
    
    for i in range(n):
        if i + 1 !=your_index:
           outgoing_shares.append(int(input("Input the recieved value from participan " + str(i + 1) + ": ")))
    
    print("Your polynom inputs: ")
    for i in range(t):
        polynom.append(int(input("Input the coefficient for x" + "^" + str(i) + ": ")))
    known_points = {your_index: calculate_point(outgoing_shares, polynom, your_index)}
    print(known_points)

    print("Your incoming points: ")
    for i in range(t - 1):
        index = int(input("Input the index for the point"))
        known_points[index] = int(input("input the value for that index"))



def calculate_point(outgoing_shares, polynom, your_index):
    point = 0
    for i in range(len(polynom)):
        point = point + polynom[i] * (your_index ** i)
        print(str(polynom[i]) + " * " + str(your_index) + " ** " + str(i))

    return(point)

main()