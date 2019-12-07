from scipy import interpolate

def lagrange(k, n, private_polynomial, shares, participants, master_points):
    shares.insert(0, private_polynomial)

    master_polynomial = interpolate.lagrange(participants, [sum(shares)] + master_points)

    print(master_polynomial)
    print(master_polynomial(0)) #(0) means setting x to 0 in the polynomial we get from master_polynomial and calculating the function

k = 5
n = 6
private_polynomial = sum([20, 18, 13, 19, 15])
shares = [34, 48, 45, 39, 24]
participants = [2, 3, 5, 6]
master_points = [1908, 7677, 50751, 101700]

lagrange(k, n, private_polynomial, shares, participants, master_points)