""""
MATH 215

Author: Reed Hunsaker

SDL 5: Spherical coordinates, parallelepiped, and cross products
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy.integrate as integrate

"""
goals:
1. Graph in 3d using a spherical coordinate change
2. Graph a plane and a parallelepiped
3. Automate the cross product and the process to find the volume of a parallelepiped
"""
def main():
    try:
        vectors = user_input()
    except ValueError and TypeError:
        print('Valus must be integers')
    area_parallelepiped(vectors[0], vectors[1])
    spherical(0, 2* np.pi,0, 2* np.pi)

def spherical(theta_start, theta_stop, phi_start, phi_stop):
    """
    The arguments are the 2 sets of bounds:

    theta_start = start radian for theta
    theta_stop = stop radian for theta
    phi_start = start radian for phi
    phi_stop = stop radian for phi

    graphs a cone as an example
    """
    theta_bounds = np.linspace(theta_start, theta_stop, 40)
    phi_bounds = np.linspace(phi_start, phi_stop, 40)
    theta, phi = theta_bounds, phi_bounds
    THETA, PHI = np.meshgrid(theta, phi)
    R = np.linspace(0, 9, 40)
    X = R * np.sin(PHI) * np.cos(THETA)
    Y = R * np.sin(PHI) * np.sin(THETA)
    Z = R * np.cos(PHI)
    #START editing code here
    """
    graph of a cone:
    """
    Z = np.sqrt(X **2 + Y ** 2)


    #STOP editing code here
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    plot = ax.plot_surface(
        X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('hot'),
        linewidth=0, antialiased=False, alpha=0.5)

    plt.show()


"""
Cross product proof:
a = [a1, a2, a3]
b = [b1, b2, b3]
x = a2b3 - a3b2
y = a3b1 - a1b3
z = a1b2 - a2b1
"""
def cross_product(a, b):
    """
    a = vector 1 in a tuple (a1, a2, a3)
    b = vector 2 in a tuple (b1, b2, b3)


    Does all the work for the cross product

    RUN this function if you want JUST THE CROSS PRODUCT

    RUN area_parallelepiped function if you want to find the VOLUME
    """
    a1 = float(a[0])
    a2 = float(a[1])
    a3 = float(a[2])
    b1 = float(b[0])
    b2 = float(b[1])
    b3 = float(b[2])
    a = [a1, a2, a3]
    b = [b1, b2, b3] 
    x = (a2*b3) - (a3*b2)
    y = (a3*b1) - (a1*b3)
    z = (a1*b2) - (a2*b1)
    x = round(x, 2)
    y = round(y, 2)
    z = round(z, 2)
    cross = (x,y,z)
    print(f'Cross product: {cross}')
    return cross

def area_parallelepiped(a,b):
    """
    Run just this function

    Calls all the function necessary to find volume 
    """
    vector3 = (1, 2, 3)
    cross = cross_product(a,b)
    area = dot_product(cross, vector3)
    print(f'Volume of parallelepiped: {area}')

def dot_product(u, v):
    """
    Arguments: u = cross product vector, v = thrid vector
    Take 2 tuples and dot product them
    """
    dot = abs((u[0] * v[0]) + (u[1] * v[1]) + (u[2] * v[2]))
    return dot


def graph_parallelepiped():
    """
    This part only got the graph of the two vectors.
    It didn't get it to look like an actual parallelpiped
    """
    x = [0,1,1,6]
    y = [0,2,1,7]
    z = [0,0,1,8]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection = '3d')
    plot = ax.scatter(x,y,z)
    ax.plot(x[0:2],y[0:2],z[0:2])
    ax.plot(x[2:], y[2:], z[2:])
    
    plt.show()

def user_input():
    """
    takes two sets of inputs from the user and changes them into tuples
    to be used later for the cross product
    """
    u = input("Please input vector one[seperate integers by comma Ex: 0,0,0]: ")
    l = u.split(',')
    new = tuple(l)
    u2 = input("Please input vector two[seperate integers by comma Ex: 0,0,0]: ")
    l2 = u2.split(',')
    n2 = tuple(l2)
    out = new, n2
    return out
main()