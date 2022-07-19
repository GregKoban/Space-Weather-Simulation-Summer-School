#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Gergely Koban'
__email__ = 'koban.gergely@wigner.hu'

from math import factorial
from math import pi
import argparse
import numpy as np

def parse_args():
    
    """Function to parse arguments from the console"""
    
    parser = argparse.ArgumentParser(description = 'Cosine approximation run from console with arguments')
    parser.add_argument('x', nargs = 1, type=float, help = 'The number inside the cosine function')
    parser.add_argument('-acc', nargs = 1, type=int, default = 10, help = 'accuracy of the approximation (default 10)')
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
acc = args.acc[0]

print(cos_approx(x, acc))

#print("Difference from numpy's cosine function:")
#print(abs(np.cos(x))-cos_approx(x,acc))



#Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':# main code block
    print("Difference from numpy's cosine function")
    print("cos(0) = ", abs(cos_approx(0)-np.cos(0)))
    print("cos(pi) = ", abs(cos_approx(pi)-np.cos(pi)))
    print("cos(2*pi) = ", abs(cos_approx(2*pi)-np.cos(2*pi)))
    print("cos(pi/2) = ", cos_approx(pi/2))