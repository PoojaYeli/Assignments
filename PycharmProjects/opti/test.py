import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def computeFunc1(x, y):
    assert x.shape == y.shape, 'x and y should be of the same size'
    out = 2*(x**3) - 6*(y**2) + 3*(x**2)*y
    return out

if __name__ == '__main__':
    x = np.arange(-10,10)
    y = np.arange(-10,10)
    X,Y = np.meshgrid(x, y)
    Z = computeFunc1(X,Y)

    # np.savetxt('pooja.txt', Y)

    if True:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

        # Customize the z axis.
        # ax.set_zlim(-10000, 10000)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

    if False:
        plt.contour(X,Y,Z, 50)

    plt.show()
    a = 10