"""
MATH 215

Author: Reed Hunsaker

SDL 4: Plotting in 3 dimensions, vectors, and eigenvalues
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy.integrate as integrate

"""
Goals:
1. Make a comprehensive 3D graph / graph a comprehensive vector field
2. Take a vector of a second dervative and find the eigenvalues
3. Determine the location of any Max min or saddle points
"""
def main():
    """
    proof of concept is being done using the graph:

    z = X^2 + 4xy + y^2

    """
    vectorfield()
    point_identification()

def vectorfield():
    """
    Graphs a vector field
    """
    x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
    
    #edit here
    #partial with respect to x
    fx = (2 * x) + (4 * y)
    #partial with respect to y
    fy = (2 * y) + (4 * x)

    graph = plt.quiver(x,y,fx,fy)
    plt.show()

"""
eginvalues calculator proof:
[dx2, dyx, dxy, dy2]
4 values & lambda
(dx2 - lambda) * (dy2 - lambda) - (dyx * dxy)
1 * (lambda **2) - (dy2 - lambda) - (dx2 - lambda) + (dx2 * dy2) - (dyx * dxy)
a = 1
b = - (dx2 + dy2)
c = - (dx2 * dy2) - (dyx * dxy)
quadradic equation:
(-b +/- sqrt((b **2) - 4 * a * c)) / a
"""
def egc():
    """


    Solves for the eigen values given dxx, dyx/dxy, dyy. 
    
    Returns the eigen values in a tuple
    """
    print("Eigenvalue calculator: ")
    print()
    # dxx = float(input("Please input the value for dxx: "))
    # dxy = float(input("Please input the value for dxy/dyx: "))
    # dyy = float(input("Please input the value for dyy: "))

    #2nd dervative values = [dxx, dxy, dyx, dyy]
    #edit here
    dxx = 2
    dxy = 4
    dyy = 2


    dyx = dxy
    secdev = (dxx, dxy, dyx, dyy)
    a = 1
    b = - (dxx + dyy)
    c = (dxx * dyy) - (dyx * dxy)
    egen = quadradic_eq(a, b, c)
    print(egen)
    return egen

def quadradic_eq(a,b,c):
    """
    quadradic equation:
    (-b±√(b^2-4ac))/2a
    """
    plus = (-b + np.sqrt((b **2) - 4 * a * c)) / (2*a)
    minus = (-b - np.sqrt((b **2) - 4 * a * c)) / (2*a)
    return plus, minus

def pointid(evalues):
    """
    evalues = eigenvalues in a tuple ex: (e1, e2)

    Takes eigenvalues in a tuple and analyzes them to determine wether they are
    a saddle point, local min, or local max.
    """
    e1 = evalues[0]
    e2 = evalues[1]
    if e1 > 0 and e2 > 0:
        print("Local Min")
    elif e1 > 0 and e2 < 0:
        print("Saddle Point")
    elif e1 < 0 and e2 > 0:
        print("Saddle Point")
    elif e1 < 0 and e2 < 0:
        print("Local Max")
    elif e1 == 0 or e2 == 0:
        print("Test Fails")
    else:
        print('Error: eigenvalues was not able to be evaluated')
    
def point_identification():
    """
    Runs the point identifation function with respect to eigenvalues inputed and tests it for the TypeError
    """
    try:
        pointid(egc())
    except TypeError:
        print('TypeError: str not accepted. Values must be int or float.')
        pass


main()