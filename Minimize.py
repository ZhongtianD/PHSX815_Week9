# imports of external packages to use in our code
from scipy.optimize import minimize
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from matplotlib import cm
#from iminuit import Minuit


# main function 
if __name__ == "__main__":
    
    def fcn(x):
        return  (2 - x[0])**2+105*(x[1]-x[0]**2)**2
    
    #It minimizes the  function 
    res = minimize(fcn,(0,0), tol=1e-6)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(0.0, 3.0, 0.05)
    y = np.arange(0.0, 6.0, 0.05)
    X, Y = np.meshgrid(x, y)
    zs = np.array(fcn((np.ravel(X), np.ravel(Y))))
    Z = zs.reshape(X.shape)
    ax.plot_surface(X, Y, Z,cmap=cm.coolwarm)
    ax.scatter(res.x[0], res.x[1], res.fun, c = 'r', marker = 'X')
    ax.scatter(2, 4, 0, c = 'r', marker = 'X', label='minimum')
    ax.set_xlabel('X ')
    ax.set_ylabel('Y ')
    ax.set_zlabel('Function value')
    ax.legend()

    ax.view_init( azim=30)

    plt.show()
    plt.savefig('minimization.png')
    
    print('The parameter is given by x='+res.x[0]+' and y='+res.x[1])
    print('function was evaluated '+res.nfev+'times')
    
    
    #Using Minuit
    #fcn.errordef = 1
    #m = Minuit(fcn, x=0,y=0)
    #m.migrad()  # run optimiser
    #print(m.values)
    
