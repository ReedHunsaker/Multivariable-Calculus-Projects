"""
MATH 215

Author: Reed Hunsaker

SDL6: Graphing curves and solving for work with a gui
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import mpmath as mp
import scipy.integrate as integrate
import tkinter as tk
x,y = np.linspace(-5,5,10), np.linspace(-5,5,10)
X,Y = np.meshgrid(x,y)
def main():
    try:
        app = tk.Tk()
        Window(app)

        app.mainloop()

    except RuntimeError as ex:
        print(type(ex).__name__, ex, sep=": ")
# """
# The gui part
# """
class Window(tk.Frame):
    """The main window of this application."""

    def __init__(self, parent):
        """Initialize a Frame object."""
        #widgets
        super().__init__(parent)
        lbltitle = tk.Label(self, text="Graphing")
        lblgtitle = tk.Label(self, text="3D Graphs:")
        lblptitle = tk.Label(self, text="Vector fileds:")
        #Grid layout for title
        lbltitle.grid(  row=0, column=0, padx=3, pady=2)
        lblgtitle.grid(row = 1, column = 0, padx=3, pady=2,columnspan=5, sticky="W")
        lblptitle.grid(row = 1, column = 1, padx=3, pady=2,columnspan=5, sticky="E")
        #Buttons with graph
        def parametric_curves(graph):
            """
            Graphs a parametric curve: (ucosv, usinv, v) 0 ≤v ≤6π and 2 ≤ u ≤ 4

            could be edited to make more user friendly
            """
            #BOUNDS
            # spiral stairs bounds
            if graph.lower() == 'stairs':
                u_bounds = np.linspace(2,4,40)
                v_bounds = np.linspace(0, 6*np.pi, 40)
            #plain bounds
            elif graph.lower() == 'plain':
                u_bounds = np.linspace(-3,3,40)
                v_bounds = np.linspace(0, 3, 40)
            #Bounds for paraboloid
            elif graph.lower() == 'paraboloid':
                u_bounds = np.linspace(0,2,40)
                v_bounds = np.linspace(0, 2*np.pi, 40)
            # bounds of half cone
            elif graph.lower() == 'cone':
                u_bounds = np.linspace(0,4,40)
                v_bounds = np.linspace(0, np.pi, 40)
            #END
            #set what is above as the bounds
            u, v = u_bounds, v_bounds
            U, V = np.meshgrid(u,v)
            #GRAPH
            #graph of a spiral stairs
            if graph.lower() == 'stairs':
                x = U * np.cos(V)
                y = U * np.sin(V)
                z = V
            elif graph.lower() == 'plain':
                x = 2*U
                y = 3*V
                z = (U**2) + (V**2)
            elif graph.lower() == 'paraboloid':
                x = U * np.cos(V)
                y = U * np.sin(V)
                z = U**2
            #Graph of half cone
            elif graph.lower() == 'cone':
                x = U
                y = U  * np.cos(V)
                z = U* np.sin(V)
            #END
            fig = plt.figure()
            ax = fig.add_subplot(111, projection = '3d')
            plot= ax.plot_surface(
                x,y,z, rstride = 1, cstride = 1, linewidth = 0,
                antialiased = False, alpha = 0.5)
            plt.show()
        def pop_button(text,x):

            """
            text = Text of button and title of graph must match that associated
            with graph in parametric_curves() function

            x = row number of button

            Makes the button and the graph 
            """
            button = tk.Button(self, text = text)
            button.grid(row=x, column = 0, padx = 3, pady = 2, columnspan = 5, sticky = "W")
            button.config(command = lambda: parametric_curves(text))
        #grid layout for graph buttons
        stairsButton = pop_button('stairs', 2)
        LHButton = pop_button('Plain', 3)
        MFButton = pop_button('Paraboloid', 4)
        PButton = pop_button("Cone", 5)
        #title and grid
        self.master.title("SDL 6")
        self.grid(padx=10, pady=10)

main()