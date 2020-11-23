"""
MATH 215

Author: Reed Hunsaker

SDL 3: Polar equations, area between 2 curves, and double integrals
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy.integrate as integrate


"""
Goals:
1. Switch (user input) Cartesian equation to polar equation.
2. Graph the polar curve and cartisean equation
3. Find the area between two curves using a double integral. 
bonus round: A function that determines the bounds of the 2 curves
"""



def main():
    print("Welcome to the Cartesian/polar program")
    po = True
    while po == True:
        print()
        choice = input('Would you like to switch a Cartesian point or polar? [C/P] (q to exit) ')
        if choice.lower() == 'c':
            CP()
        elif choice.lower()=='p':
            PC()
        elif choice.lower() =='q':
            break
        else:
            print('I do not understand your input please try again.')
    polar_plot()
    Cartesian()

#Cartesian to Polar switching function
def CP():
    """
    Takes a Cartesian point and changes it to a polar point.
    Graphs the point for comparison.
    """
    x = float(input('Please input a x value: '))
    y = float(input('Please input a y value: '))
    r = np.sqrt((x * x) + (y * y))
    r = round(r, 2)
    theta = math.atan(y / x)
    thetad = (theta * 180) / np.pi
    if theta == -0.0:
        theta = np.pi
        thetad = 180
    if x < 0 and y < 0:
        theta += np.pi
        thetad += 180
    thetad = round(thetad, 2)
    theta = round(theta, 3)
    print(f'The polar coordinates for this point are: ({r}, {theta}) or ({r}, {thetad}°)')
    plt.polar(theta, r, marker = 'o', markersize = 5, color = 'black')
    plt.annotate(f'({r}, {thetad}°)', (theta, r))
    plt.grid(True)
    plt.title(f'({x},{y}) in polar')
    plt.show()

#Polar to cartesian switching function
def PC():
    """
    Takes a polar point and graphs it in Cartesian.
    Plots the point for comparison.
    """
    r = float(input('Please input the radius: '))
    theta = float(input('Please input theta in degrees: '))
    theta = (theta * np.pi) / 180
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    x = round(x, 2)
    y = round(y, 2)
    print(f'The cartesian coordinates for this point are: ({x}, {y})')
    plt.plot(x,y, marker='o', markersize = 3, color = 'black')
    plt.grid(True)
    plt.title(f'({r}, {theta}°) in Cartesian')
    plt.annotate(f'({x}, {y})', (x,y))
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

#Taking a polar eqation and graphing it in cartisan
def Cartesian():
    theta = np.linspace(0, 2* np.pi)
    # r = np.linspace(0, 10)
    r = 3 * np.cos(theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x,y)
    plt.grid(True)
    plt.title("A Cartesian Graph")
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

# plotting two polar curves on the same graph
def polar_plot():
    """
    The graph of two polar curves
    """
    theta = np.linspace(0, 2* np.pi)
    r = 3 * np.cos(theta)
    r2 = 1 * (np.cos(theta) **2) * (np.sin(theta)**2)
    plt.polar(theta,r, theta, r2)
    plt.grid(True)
    plt.title("A Polar Graph (Orange = circle?)")
    plt.show()

#Trying to graph a polar graph
def polar_plot2():
    theta = np.linspace(0 , 2 * np.pi)
    r = 1 * (np.cos(theta) **2) * (np.sin(theta)**2)
    plt.polar(theta, r)
    plt.grid(True)
    plt.title('Circle')
    plt.show()

#working to get the double integral funciton to work
def area():
    theta = np.linspace(0, 2* np.pi)
    r1 = 3 * np.cos(theta)
    r2 = 1 * (np.cos(theta) **2) * (np.sin(theta)**2)
    y = r1, r2
    a = integrate.dblquad(y, 1, r1, lambda x: 0, lambda x: 2 * np.pi)
    a= a[0]
    print(f"The area is {a}")

main()