"""
MATH 215

Author: Reed Hunsaker

SDL 01: program that solves for the angle between two 2D vectors.
"""
import math
import matplotlib.pyplot as plt
import numpy as np

#Function to solve the dot product
def Dot_Product (x,y,a,b):
    #Perfroms the dot product
    #takes the absolute value of the dot product

    DProduct = abs((x * a) + (y * b))

    return DProduct

#Finds the Magnitude of the vector
def Magnitude (x,y,a,b):
    #finds the magnitude of the first vector

    Mag1 = ((x ** 2 )+ (y ** 2)) ** 0.5

    #Find the magnitude of the second vector

    Mag2 = ((a ** 2) + (b ** 2)) ** 0.5

    #Mulitplies the magnitudes together to be used in the Law of cosine

    Magfinal = Mag1 * Mag2

    return Magfinal

#Calculates the law of cosine
def Law_of_Cosine (DP,M):
    #DP is Dot product and M is magnitude
    #This is the formula for the Law of Cosine
    u = (DP) / M
    LOC = math.acos(u)

    #This turns it from radians into degrees 

    LOC = LOC * (180/math.pi)

    return LOC



#User inputs the values of the two vectors
#can be integers or numbers with decimals

x = float(input("What is the first value of the first vector? "))
y = float(input ("Second value of the first vector? "))
a = float(input("First value of the second vector? "))
b = float(input('Second value of the second vector? '))

#Blank line to make final output more readable
print()

#Calls the Dot Product function and is set equal to the dot product of the vectors
DotProduct = Dot_Product(x,y,a,b)

#Calls the Magnitude function and is set equal to the magnitude of the vecotrs
Magnitude_of_Vector = Magnitude(x,y,a,b)


#Calculates the angle between the vector in degrees
Angle = Law_of_Cosine(DotProduct, Magnitude_of_Vector)

#display and round to two decimal places
print(f'The angle between the two vecotrs is: {Angle:.2f} degrees') 
print(f'The dot product of the two vectors is: {DotProduct:.2f}')
print(f'The magnitude of the two vectors is:{Magnitude_of_Vector:.2f}')
#blank line
print()

def plot(v1,v2,r1,r2):
    orgin = [0], [0]
    ax = plt.axes
    plt.grid()
    plt.title("The Law of Cosines by: Reed Hunsaker", fontsize=10)
    u1 = np.array((v1))
    u2 = np.array((v2))
    u3 = np.array((r1))
    u4 = np.array((r2))
    #graphs the vecotrs using the quiver function 
    q1 = plt.quiver(*orgin, u1, u2, scale = 1)
    # plt.quiverkey(q1, X = 0.1, Y = 0.3, U = 10, label="Vector 1")
    plt.quiver(*orgin, u3, u4, scale = 1)
    plt.xlim = (-10, 10)
    plt.ylim = (-10, 10)
    plt.show()

plot(x,y,a,b)