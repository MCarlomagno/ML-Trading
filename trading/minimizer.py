import scipy.optimize as spo
import numpy as np
import matplotlib.pyplot as plt

def fun(X):
	Y = (X - 1.5)**2 + 0.5
	print("X: {}, Y: {}".format(X,Y))
	return Y

def test_run():
	Xguess = 2.0
	min_result = spo.minimize(fun, Xguess, method="SLSQP", options= {'disp': True})
	print("min result founded at: X = {}, Y = {}".format(min_result.x,min_result.fun))
	Xplot = np.linspace(0.5,2.5,21)
	Yplot = fun(Xplot)
	plt.plot(Xplot, Yplot)
	plt.plot(min_result.x, min_result.fun, 'ro')
	plt.show()

if __name__ == '__main__':
	test_run()