

def main():
    n = int(input("Input the number of participants: "))
    t = int(input('Input the thresholdvalue: '))
    your_index = int(input("Input your participation number: "))
    
    incoming_shares = []
    outgoing_shares = []
    polynom = []

    for i in range(n):
        if i  + 1 !=your_index:
           outgoing_shares.append(input("Input the value of your polynome for participan " + str(i + 1) + ": "))
    
    for i in range(n):
        if i + 1 !=your_index:
           outgoing_shares.append(input("Input the recieved value from participan " + str(i + 1) + ": "))
    
    print("Your polynom inputs: ")
    for i in range(t):
        input("Input the coefficient for x" + "^" + str(i) + ": ")

main()