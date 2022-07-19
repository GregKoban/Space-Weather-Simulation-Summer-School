#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Gergely Koban'
__email__ = 'koban.gergely@wigner.hu'

from math import factorial
from math import pi
import argparse
import matplotlib.pyplot as plt

def parse_args():
    
    """Function to parse arguments from the console"""
    
    parser = argparse.ArgumentParser(description = 'Cosine approximation run from console with arguments')
    parser.add_argument('x', nargs = 1, type=float, help = 'The number inside the cosine function')
    parser.add_argument('-accmin', nargs = 1, type=int, default = 10, help = 'minimum accuracy of the approximation (default 10)')
    parser.add_argument('-accmax', nargs = 1, type=int, default = 11, help = 'mmaximum accuracy of the approximation (default 20)')
    args = parser.parse_args()
    
    return args

def cos_approx(x, accuracy=10):
    """This program returns an approximation of cosine using Taylor approximation with a given accuracy"""
    elements = [(((-1)**n)*x**(2*n))/(factorial(2*n)) for n in range(accuracy+1)] #using Taylor approximation
    #then I make a summary of the elements
    
    return sum(elements)

args = parse_args()

print(args)

x = args.x[0]
accmin = args.accmin[0]
accmax = args.accmax[0]

result = []
accnow = []

for acctmp in range(accmin, accmax):
    accnow.append(acctmp)
    result.append(cos_approx(x, acctmp))
    
plt.plot(accnow, result)
plt.xlabel(r'Number of terms')
plt.ylabel(r'Approximation result')
plt.title('Cosine approximation')
plt.show()



