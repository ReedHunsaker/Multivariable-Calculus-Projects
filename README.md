# SDL

Must have python3 downloaded to use the code

To use the code make sure you have a few libaries downloaded:
1. matplotlib 
2. numpy
3. math
4. mpmath
5. scipy
6. sympy

you can use these commands to download these libaries:

python3 -m pip install -U pip

python3 -m pip install -U matplotlib

pip3 install numpy

pip insall mpmath

pip install scipy

pip install sympy

(The Math libary should be built into python)

SDL1 - Dot product and vectors:
The program will print these the resluts for two vectors and graph it:

1.Dot product

2.Magnitude

3.Law of cosine


Disclaimer:

The graph size will have to be adjusted manually if it exceeds the window and all vectors have a base at the orgin.

SDL2 - Conics and Arc length
The program will ask the user which of 4 graphs they want to view. 

It will then return the graph with it's arc length in the title.

the function work is not finished but would have calculated the work of the curve in a given vector field

SDL3 - Cartesian and Polar plots
The program takes a point in either Cartesian or polar and graphs it in the opposite coordinate system.

The program will return a plot of the point in the coorisponding coordinate system.

There are also several uncomplete functions to graph and take the double integral of some polar and cartesian curves.


SDL 4 - Vetor fields and eigenvalues calculator

The function graphs a vector field by taking in the dervative with respect to x and y

Also solves for eigenvalues given dxx, dxy, dyx, and dyy

All functions are complete

SDL 5 - Solving cross product, area of a parallelepiped, and graphing in 3D

The program ask for the user to input 2 vectors in the form of comma seperated values example input: 0,0,0

Solves for the cross poduct of the two vectors as well as the area of a parallelpiped using a vecotor (1,2,3) 

Graphs a cone as a proof of concept of the spherical coordinate graphing in python

Feel free to play around with the graphing in 3D by changing the code on line 51 or changing the bounds in the function called on line 26

All functions are complete (except graph_parallelepiped() which only graphs two line segmants)
