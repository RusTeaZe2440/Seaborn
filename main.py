import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


x = np.linspace(-10,10,50)
y = np.linspace(-10,10,50)
X,Y = np.meshgrid(x,y)
z = X ** 2 + Y **2

def create_surface_plot(x:np.linspace,y:np.linspace,z) -> None:
    fig = plt.figure(figsize=(8,8))
    axs = fig.add_subplot(2,2,1,projection='3d')
    axs.plot_surface(x,y,z,cmap='autumn_r')

    ax2 = fig.add_subplot(2,2,2)
    ax2.contourf(x,y,z, cmap='autumn_r')

create_surface_plot(X,Y,z)
