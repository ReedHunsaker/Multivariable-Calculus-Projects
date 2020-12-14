"""
Math 215

Author: Reed Hunsaker

SDL 6:
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy.integrate as integrate

"""
Goals:
1. Graph parametrized curves ( Ex: (ucosv, usinv, v) 0 ≤v ≤6π and 2 ≤ u ≤ 4 
or (t,v)=(3cost,3sint,v)  for 0≤t≤2π and 1≤v≤4.)
or (t)=(3cost,3sint,t)  for 0≤t≤6
2. Graph a vector field along with a curve and solve for the work done along the curve
Ex: F = (4x+3xy, x**2 + 2y) r(t) = (3t - 1, 5t+2) for 0≤t≤1 (end ==3) [December 7th brain gains]
3. Graph a vector field and use greens therom to find the work done along a rectangle, circle, and triangle
F = (3x + 4y, 6X + 7y) [December 8th brain gains]
area_rectangle = b*h
area_circle = 1/2 πr**2
area_triangle = 1/2 b*h
"""
#Universly define X and Y for all functions
x,y = np.linspace(-5,5,10), np.linspace(-5,5,10)
X,Y = np.meshgrid(x,y)
def main():
    # parametric_curves()
    vector_feild(3*X + 4*Y, 6*X + 7 * Y, 't', curve= True)
    work_dos()


def parametric_curves():
    """
    Graphs a parametric curve: (ucosv, usinv, v) 0 ≤v ≤6π and 2 ≤ u ≤ 4

    could be edited to make more user friendly
    """
    #BOUNDS
    # spiral stairs bounds
    u_bounds = np.linspace(2,4,40)
    v_bounds = np.linspace(0, 6*np.pi, 40)
    #plain bounds
    # u_bounds = np.linspace(-3,3,40)
    # v_bounds = np.linspace(0, 3, 40)
    #Bounds for paraboloid
    # u_bounds = np.linspace(0,2,40)
    # v_bounds = np.linspace(0, 2*np.pi, 40)
    # bounds of half cone
    # u_bounds = np.linspace(0,4,40)
    # v_bounds = np.linspace(0, np.pi, 40)
    #END
    u, v = u_bounds, v_bounds
    U, V = np.meshgrid(u,v)
    #GRAPH
    #graph of a spiral stairs
    x = U * np.cos(V)
    y = U * np.sin(V)
    z = V
    #Graph of plane
    # x = 2*U
    # y = 3*V
    # z = (U**2) + (V**2)
    #graph of a paraboloid
    # x = U * np.cos(V)
    # y = U * np.sin(V)
    # z = U**2
    #Graph of half cone
    # x = U
    # y = U  * np.cos(V)
    # z = U* np.sin(V)
    #END
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    plot= ax.plot_surface(
        x,y,z, rstride = 1, cstride = 1, linewidth = 0,
        antialiased = False, alpha = 0.5)
    plt.show()

def vector_feild(dx,dy, shapes = False, curve = False):
    """
    dx = dx part of vector field (use big X and Y as well as order of operations)

    dy = dy part of vector field (use big X and Y as well as order of operations)

    shapes = c,r, or t (circle, rectangle, or triangle)

    (curve = true) to plot the vector over the vector field

    Function to graph vector_field
    """
    x,y = np.linspace(-5,5,10), np.linspace(-5,5,10)
    X,Y = np.meshgrid(x,y)

    # fx = 4*X + 3*X*Y
    # fy = (X**2) +2*Y
    fx = dx
    fy = dy
    graph = plt.quiver(X,Y,fx,fy)
    if curve == True:
        curves(0,1)
    if shapes != False:
        if shapes == 'c':
            geoshapes(c= True)
        elif shapes == 'r':
            geoshapes(r = True)
        elif shapes == 't':
            geoshapes(t = True)
    plt.show()
def curves(a, b):
    """
    a = lower bound
    b = upper bound


    Displays a curve paramterized as r(t) = (rx,ry) from a ≥ t ≥ b
    """
    t = np.linspace(a,b,40)
    #edit here to change curve
    rx = 3*t - 1
    ry = 5 * t + 2
    #STOP
    graph = plt.plot(rx,ry)
def geoshapes(c = False, r = False, t = False):
    """
    Function displays a graph based on that determined by the user when calling the vector_field function
    """
    if c == True:
        circle = plt.Circle((0,0), radius = 3, fill = None, edgecolor = 'y')
        plt.gca().add_patch(circle)
    elif r == True:
        rectangle = plt.Rectangle((0, 0), 5, 5, fill = None, edgecolor='r')
        plt.gca().add_patch(rectangle)
    elif t == True:
        points = [[0,0], [0,3], [3,3]]
        triangle = plt.Polygon(points, fill = None, edgecolor = 'r')
        plt.gca().add_patch(triangle)
    else:
        print('Error: please input a True value for either c, r , or t')
def work_dos():
    """
    Solves for the work given the potential from the last problem on December 7th Brain Gains
    """
    #potential = 2x**2+x**2y+y**2
    x1,y1 = (2, -3)
    x2,y2 = (-1, 2)
    p1 = (2*(x1**2)) + ((x1**2)*y1) + (y1**2)
    p2 = (2*(x2**2)) + ((x2**2)*y2) + (y2**2)
    sol = p1 - p2
    sol = abs(sol)
    print(f'The vector field F=(4x+2xy,x2+2y) \n'
    'along the curve C parametrized by r(t)=(3t−1,−5t+2) \n '
    f'for 0 ≤ t ≤ 1 is: {sol}')

main()