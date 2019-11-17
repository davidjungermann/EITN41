#How many iterations (how many balls thrown) does it take before you generate c = 1, 100 and 10,000?

import numpy as numpy

c = input("Input the provided c: ")
u = input("Input the provided u: ")
k = input("Input the provided k: ")
interval_width = input("Input the provided confidence interval width: ")
lambda_value = 3.66

def create_bins():
    exp = 2 ** int(u)
    bins = numpy.empty(exp, dtype=int)
    return bins
    
create_bins()
