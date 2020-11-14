"""
MATH 215

Author: Reed Hunsaker

SDL 02: Conics, arc length, and Work
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy.integrate as integrate
"""
Goals:
1. graph a curve using parametric equations
2. Solve an arc length integral in python
3. Solve a work integral (dot product F . D)
"""

def main():
    """
    User chooses from the 4 graphs which will 
    be displayed along with the arc length
    """
    con = True
    while con == True:
        select = input("Pick a graph [PARABOLA, ELLIPSE, HYPERBOLA, 2.20]: ")
        if select.lower() == "parabola":
            parabola()
            con = False
        elif select.lower() == "ellipse":
            ellipse()
            con = False
        elif select.lower() == "hyperbola":
            hyperbola()
            con = False
        elif select == "2.20":
            graph_desc = "p20"
            problem_twenty()
            con = False
        else:
            print('That is not a valid input.')
            con = True

def parabola():
    """
    Graph of parabola with arc length
    from: 2.21 #1
    """
    #could I have the user input parametrizations in term of t?
    graph_desc = 'parabola'
    t = np.linspace(0, 3)
    #paramiterization
    x = t
    y = t ** 2
    #build the graph
    plt.plot(x,y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title(f'Parabola arc length = {round(arc_length(graph_desc, 3, 0),3)}')
    plt.grid(True)
    plt.show()

def ellipse():
    """
    Graph of ellipse with arc length
    from: 2.20 #2
    """
    graph_desc = 'ellipse'
    t = np.linspace(0, 2*np.pi)
    #paramiterization
    x = 4*np.cos(t)
    y = 5*np.sin(t)
    #build the graph
    plt.plot(x,y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title(f'Ellipse arc length = {round(arc_length(graph_desc, 2*np.pi, 0), 3)}')
    plt.grid(True)
    plt.show()

def hyperbola():
    """
    Graph of hyperbola with arc length
    from: 2.21 #3
    """
    graph_desc = 'hyperbola'
    t = np.linspace( -1 * np.pi /4, np.pi / 4, 100)
    #paramiterization
    x = np.tan(t)
    y = 1/np.cos(t)
    #build the graph
    plt.plot(x,y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title(f'Hyperbola arc length = {round(arc_length(graph_desc, np.pi /4, -1 * np.pi / 4 ), 3)}')
    plt.grid(True)
    plt.show()

def problem_twenty():
    """
    Graph of problem 2.20 with arc length
    """
    graph_desc = "p20"
    t = np.linspace(2, 5)
    #paramiterization
    x = t**3
    y = (3* (t **2)) / 2
    #build the graph
    plt.plot(x,y)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title(f'Problem 2.20 arc length = {round(arc_length(graph_desc, 5, 2), 3)}')
    plt.grid(True)
    plt.show()

def arc_length(graph, a ,b):
    """
    Finds the arc length of the given functions between certain

    arg graph = pick graph key = [parabola, ellipse, hyperbola, p20]

    arg a = the upper bound of the arc length

    arg b = the lower bound of the arc length

    dx/dt and dy/dt were calculated by hand
    """
    if graph == 'parabola':  
        parabola_al = integrate.quad(lambda x: mp.sqrt(1+(2*x)**2), b, a)
        p_al = parabola_al[0]
        print(p_al)
        return p_al
    elif graph == 'p20':
        p20_al = integrate.quad(lambda x: mp.sqrt((3*x)**2 + (3*x)**2), b, a)
        p2_al = p20_al[0]
        return p2_al
    elif graph == "ellipse":
        ellipse_al = integrate.quad(lambda x: mp.sqrt((-4*np.sin(x))**2 + (5*np.cos(x))**2), b,a)
        el_al = ellipse_al[0]
        return el_al
    elif graph == "hyperbola":
        hyperbola_al = integrate.quad(lambda x: mp.sqrt((1/(np.cos(x))**2)**2 + (np.tan(x)*(1/np.cos(x)))**2), b,a )
        hyper_al = hyperbola_al[0]
        return hyper_al

def work(a, b):
    """
    Takes the conics and finds the work along them given a Force vector field

    UNFINISHED:
    Vector field is working
    Integral with dot product is not
    """
    # vector Field
    i,j = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))

    u = i/np.sqrt(i**2 + j**2)
    v = -j/np.sqrt(i**2 + j**2)

    plt.quiver(i,j,u,v)

    #integration

    parabola_work = integrate.quad(lambda x: (x * (x/np.sqrt(x**2 + x**2)) + (x**2 * -x/np.sqrt(x**2 + x**2))), b, a)
    print(f'The work along the parabola from {a} to {b} is: {parabola_work[0]}')
    plt.show()


main()